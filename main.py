import socket

port = 53
loopback_ip = '127.0.0.1'

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((loopback_ip, port))

while True:
    data, address = sock.recvfrom(512)
    print(data)
    print(address)