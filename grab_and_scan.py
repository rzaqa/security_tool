from utils import timefunc
from port_scanner import Scanner
from grabber import Grabber


@timefunc
def main():
    ip = "10.206.90.40"
    portrange = (1, 3)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error", e)


if __name__ == "__main__":
    main()
