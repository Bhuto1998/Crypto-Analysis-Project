# For this we need to install RC6Encryption package
from RC6Encryption import RC6Encryption
from hashlib import sha256

plaintext = "YellowSubmarines"
plaintext_toliteral = plaintext.encode()
print(plaintext_toliteral)
rc6 = RC6Encryption(sha256(plaintext_toliteral).digest())
cipher = rc6.blocks_to_data(rc6.encrypt(plaintext_toliteral))
decipher = rc6.blocks_to_data(rc6.decrypt(cipher))
print(decipher.decode())

#This code is not final as it doesn't take a key