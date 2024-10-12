import socket
import select

host = "127.0.0.1"

ip_addr = socket.gethostbyname(host)

'''
Create a simple server socket and listen for incoming connections
'''
def test_socket_modes():
    # Creates a TCP socket for IPv4 communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Sets the socket to blocking mode. This means that the s.listen() call will block until a client connects.
    s.setblocking(1)
    
    # If no event occurs within this time (0.5), a socket.timeout exception will be raised.
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print ("Trivial Server launched on socket: %s" %str(socket_address))
    while(1):
        s.listen(1)

# Check if a port is open or not
def check_if_port_is_open():
    port_n = int(input("Enter port number: "))
    try:
        s = socket.socket()
        r = s.connect((ip_addr, port_n))
        print("Port {} connected".format(port_n))
        s.close()
    except:
        print("Port {} disconnected".format(port_n))

def TCP_socket_example():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    s.bind((host, 9050))
    
    # This method tells the socket to start listening for incoming connection requests. 
    # 5: maximum number of pending connections that can be queued before the server starts refusing new connections.
    s.listen(5)
    
    client_sk, client_addr = s.accept()
    print("Client {} connected".format(client_addr))
    
    data = "Hello Client!"
    client_sk.send(data.encode('UTF-8'))
    
    data = client_sk.recv(4096)
    print("Received {} from {}".format(data.decode('UTF-8'), client_addr))
    client_sk.close()
    s.close()

def temp_func():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    s.connect((host, 9050))
    
    data = s.recv(4096)
    print("Received {} from {}".format(data.decode('UTF-8'), host))
    
    data = "Hello Server"
    s.send(data.encode('UTF-8'))
    s.close()

if __name__ == "__main__":
    TCP_socket_example()
    temp_func()