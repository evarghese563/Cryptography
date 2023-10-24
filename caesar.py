'''The Implementation of the Caesar cipher'''

def encrypt():

    print("input M")
    m = int(input())
    encrypt = (m + 1305)%26

    print(encrypt)

def decrypt():

    print("input C")
    c = int(input())
    decrypt = (c - 1305)%26

    print(decrypt)


if __name__ == '__main__':

    # encrypt()
    decrypt()
