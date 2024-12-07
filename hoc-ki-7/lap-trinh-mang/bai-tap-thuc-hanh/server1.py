import cv2
import socket #For network communication.
import pickle # For serializing and deserializing Python objects.
import struct #For packing and unpacking binary data.

# Set up the server socket: IPv4 in TCP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '0.0.0.0'  # Listen on all network interfaces
port = 9999

#Bind the socket to the specified host (0.0.0.0 for all interfaces) and port (9999).
server_socket.bind((host_ip, port))

#Start listening for incoming connections
server_socket.listen(5)
print("Server listening on port:", port)

# Accept a connection from the client
client_socket, addr = server_socket.accept()
print('Connection from:', addr)

data = b""
payload_size = struct.calcsize("Q") #64-bit unsigned integer format

while True:
    # Retrieve the message size
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # 4K bytes
        if not packet:
            break
        data += packet

    if len(data) < payload_size:
        break

    # Unpack the payload size to get the frame size
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0] #unpacks these bytes to get the actual message size.

    # Retrieve the entire frame data
    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)

    # Extract the frame data
    frame_data = data[:msg_size] #binary representation of a single video frame
    data = data[msg_size:] 

    # Deserialize the frame
    frame = pickle.loads(frame_data)

    # Display the frame
    cv2.imshow("Server - Receiving Video", frame)

    # Stop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q")
        break
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()
