import socket

from utils import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                print(f"Port {port} is open")
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        print(f"For port {port} result is - {result}")
        s.close()
        return result == 0

    def write(self, filepath):
        openports = map(str, self.open_ports)
        with open(filepath, "w") as f:
            f.write("\n".join(openports))


@timefunc
def main():
    ip = "10.206.90.40"  # You can put here you IP address
    # ip = "192.168.1.172"  # You can put here you IP address
    scanner = Scanner(ip)
    # scanner.scan(1, 65000)
    scanner.scan(1, 1000)
    # print(repr(scanner))
    print(scanner.open_ports)
    scanner.write('open_ports.txt')


if __name__ == "__main__":
    main()
