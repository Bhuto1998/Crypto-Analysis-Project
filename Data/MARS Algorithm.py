# This code contains implementation of the MARS cipher
# We need to install the following package: github.com/ricmoo/pyaes
#Still need to check whether this is the implementation of MARS
import os
import pyaes


key = os.urandom(16)

PlainText = "TextMustBe16Byte"
aes = pyaes.AESModeOfOperationECB(key)
ciphertext = aes.encrypt(PlainText)

print("This is the final cipher text: {0}".format(ciphertext))

decrypted = aes.decrypt(ciphertext)

print("This is the decrypted file: {0}".format(decrypted))

#Now lets check whether plain text and the decrypted cipher texts are the same

print(decrypted.decode() == PlainText)


