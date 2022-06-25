import string
import random
import hashlib

chars = string.ascii_letters + string.digits + string.punctuation
def random_char(x):
    return ''.join(random.choice(chars) for y in range(x))

lenght = int(input("Password Lenght?: "))

passwd = random_char(lenght)

print("your password is: " + passwd)

ans = input("Would you like to see the different hashes for it? (Y/N)\n")

if ans == "y" or ans == "Y":
    encoded = passwd.encode()

    hash1 = hashlib.sha1(encoded).hexdigest()
    hash256 = hashlib.sha256(encoded).hexdigest()
    hash512 = hashlib.sha512(encoded).hexdigest()
    hashMD5 = hashlib.md5(encoded).hexdigest()

    print("Hash SHA1: " + hash1)
    print("Hash SHA256: " + hash256)
    print("Hash SHA512: " + hash512) 
    print("Hash MD5: " + hashMD5)