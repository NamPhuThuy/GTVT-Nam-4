import socket
import select

host = 'localhost'
port = 9050

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

inputs = [s]
outputs = []
errors = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, errors)

    for sock in readable:
        if sock is s:
            client_sk, client_addr = s.accept()
            print("Client {} connected".format(client_addr))
            inputs.append(client_sk)
        else:
            data = sock.recv(4096)
            if data:
                print("Received {} from {}".format(data.decode('UTF-8'), sock.getpeername()))
                sock.send(data)
            else:
                print("Closing connection from {}".format(sock.getpeername()))
                inputs.remove(sock)
                sock.close()

    for sock in exceptional:
        print("Error occurred with {}".format(sock.getpeername()))
        inputs.remove(sock)
        sock.close()