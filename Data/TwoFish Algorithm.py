#For this we need to install Twofish library
from twofish import Twofish
key = "*secret*"
key = key.encode()
plaintext = "YellowSubmarines"
T = Twofish(key)
x = T.encrypt(plaintext.encode())
print(T.decrypt(x).decode())