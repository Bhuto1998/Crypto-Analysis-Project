import base64
from py3rijndael import Rijndael
#Using 16 bit Key
key = '*secret*12345678'
rijndael = Rijndael(key.encode(),block_size=16)
plain_text = "YellowSubmarines"
plain_text_literal = plain_text.encode()

cipher = rijndael.encrypt(plain_text_literal)
cipher_text = base64.b64encode(cipher)
print(cipher_text)
temp = rijndael.decrypt(cipher)

print(temp)