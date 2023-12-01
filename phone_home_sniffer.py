import socket

from nettypes import EthernetFrame


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    host = '10.0.10.140'
    port = 8080
    forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward.connect((host, port))
    while True:
        data, addr = conn.recvfrom(65535)
        if data:
            eth = EthernetFrame(data)
            print(eth)


if __name__ == "__main__":
    main()








