import socket

if __name__ == '__main__':
    s= socket.socket( socket.AF_INET ,socket.SOCK_STREAM ,0)
    s.bind(('127.0.0.1',9050))

    while True:
        try:
            s.listen(5)
            client_sk , client_addr = s.accept()
        except s.error as e:
            print("connect fail {}".format(e))
        print("client address:{}".format(client_addr))

        # data = "hello client"
        while True:
            data = input("enter code:")
            client_sk.send(data.encode('utf-8'))

            data = client_sk.recv(4096)
            print("receive from client:")
            print(data.decode('utf-8'))

            if(data.decode('utf-8')== "bye"):
                # client_sk.send(data.encode('bye'))
                client_sk.close()
                break
    s.close()