import socket
from capture import PCAPFile

# By sniffing packets you can save information to a file which can be readable by Wireshark application
# May not work on MacOs, because of AF_PACKET


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # conn = socket.socket(socket.SOCK_RAW, socket.ntohs(3))
    pcap = PCAPFile('packets.pcap')
    while True:
        raw_data, addr = conn.recvfrom(65535)
        pcap.write(raw_data)
    pcap.close()


if __name__ == "__main__":
    main()
