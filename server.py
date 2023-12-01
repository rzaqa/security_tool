import socket


class Server:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def serve(self):
        hostport = (self.host, self.port)
        self.socket.bind(hostport)
        self.socket.listen(1)
        conn, addr = self.socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data:
                    print(data)
        self.socket.close()


if __name__ == "__main__":
    server = Server('localhost', 8081)
    server.serve()  # then you need send a command in CLI $ nc localhost 8080
    # print()
