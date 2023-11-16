import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    # host = '8.8.8.8'
    port = 11000
    # try:
    #     s.connect((host, port))
    #     print('it works')
    # except Exception as e:
    #     print(e)
    #     print(e.args)
    #     print(e.__cause__)

    # second example how to create s socket connection
    result = s.connect_ex((host, port))
    print('Result is {}'.format(result))   # will show '0' if connection was successfull
    s.close()


if __name__ == "__main__":
    main()
