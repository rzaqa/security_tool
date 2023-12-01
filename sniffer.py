import socket
from capture import PCAPFile
from nettypes import EthernetFrame, IPHeader, TCPSegment, UDPSegment


# By sniffing packets you can save information to a file which can be readable by Wireshark application
# May not work on MacOs, because of AF_PACKET


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # conn = socket.socket(socket.SOCK_RAW, socket.ntohs(3))
    pcap = PCAPFile('packets.pcap')
    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethframe = EthernetFrame(raw_data)
        # print(ethframe.__dict__)
        # print(ethframe)
        if ethframe.protocol == 8:
            ipheader = IPHeader(ethframe.leftover_data)
            print(ipheader)
            if ipheader.protocol == 6:
                tcp = TCPSegment(ipheader.leftover_data)
                if tcp.src_port == 80:
                    print(tcp)
            elif ipheader.protocol == 17:
                udp = UDPSegment(ipheader.leftover_data)
                print(udp)
        # break
        # pcap.write(raw_data)
    pcap.close()


if __name__ == "__main__":
    main()
