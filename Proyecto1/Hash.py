import getpass
import hashlib

passwd = getpass.getpass("Password: ")

print("Password:" + passwd)

encoded = passwd.encode()

hash256 = hashlib.sha256(encoded).hexdigest()
hash512 = hashlib.sha512(encoded).hexdigest()

print("Hash SHA256: " + hash256)
print("Hash SHA512: " + hash512) 