import os
import pyaes
import base64
from py3rijndael import Rijndael


key = "*secret*12345678"
#Reading Plain Text
path = "/Users/bhutoriyamukherjee/PycharmProjects/Crypto Analysis Project/Data/PlainText"
filename = "plain-0.txt"
fpath = os.path.join(path,filename)
f = open(fpath)
content = f.read()
print(content)
f.close()

n =16
split_string = [content[i:i + n] for i in range(0, len(content), n)]
print(split_string)
PlainText = split_string[0]
key_literal = key.encode()
aes = pyaes.AESModeOfOperationECB(key_literal)
ciphertext = aes.encrypt(PlainText)
ciphertext2 = base64.b64encode(ciphertext)
print(ciphertext2)
#print(ciphertext.decode())
#print(key)

rijndael = Rijndael(key.encode(),block_size=16)
plain_text = split_string[1]
plain_text_literal = plain_text.encode()

cipher = rijndael.encrypt(plain_text_literal)
#print(cipher)
cipher_text = base64.b64encode(cipher)
print(cipher_text)