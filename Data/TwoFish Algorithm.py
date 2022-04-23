#For this we need to install Twofish library
from twofish import Twofish
key = "*secret*12345678"
key = key.encode()
plaintext = "YellowSubmarines"
T = Twofish(key)
x = T.encrypt(plaintext.encode())
print(x)
print(T.decrypt(x).decode())