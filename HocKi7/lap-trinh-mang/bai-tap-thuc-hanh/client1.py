import cv2
import socket
import pickle
import struct

# Initialize the video capture
cap = cv2.VideoCapture(0)  # creates a video capture object using the default webcam (index 0).

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'  # Replace with the server's IP address
port = 9999
client_socket.connect((host_ip, port))

while cap.isOpened():
    res, frame = cap.read() #Reads a frame from the webcam and stores the status (success) and the captured frame in ret and frame variables, respectively.
    if not res:
        break

    # Serialize the frame
    data = pickle.dumps(frame)

    # Send message length first, then the serialized data
    message = struct.pack("Q", len(data)) + data #64-bit unsigned integer
    client_socket.sendall(message) 

    # Display the frame on the client side as well (optional)
    cv2.imshow('Client - Sending Video', frame)

    # Stop if 'c' is pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print("C")
        break
cap.release()
client_socket.close()
cv2.destroyAllWindows()
