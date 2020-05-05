from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from hashlib import md5
from random import choice

chars = ascii_lowercase + ascii_uppercase + digits + punctuation

def salt_shaker():

    hash_salt = ''.join(choice(chars) for i in range(10))

    return hash_salt


def pw_hasher(salted_pw):

    return md5(salted_pw.encode()).hexdigest()


if __name__ == '__main__':
    pw = input()
    salt = salt_shaker()
    print(pw_hasher(pw + salt))
