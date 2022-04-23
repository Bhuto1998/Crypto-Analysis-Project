import os
import pyaes
import base64
from py3rijndael import Rijndael
from twofish import Twofish


key = "*secret*12345678"
path = "/Users/bhutoriyamukherjee/PycharmProjects/Crypto Analysis Project/Data/PlainText Large"

for i in range(220):
    try:
        filename = "plainLarge-" + str(i) + ".txt"
        fpath = os.path.join(path, filename)
        f = open(fpath)
        content = f.read()
        f.close()
        n = 16
        split_string = [content[i:i + n] for i in range(0, len(content), n)]
        temp_MARS = ""
        temp_Rijndael = ""
        temp_Twofish = ""
        for el in split_string:
            # Running MARS
            key_literal = key.encode()
            aes = pyaes.AESModeOfOperationECB(key_literal)
            ciphertext = aes.encrypt(el)
            ciphertext2 = base64.b64encode(ciphertext)
            temp_MARS = temp_MARS + ciphertext2.decode()
            # Running Rjndael
            rijndael = Rijndael(key.encode(), block_size=16)
            plain_text_literal = el.encode()
            cipher = rijndael.encrypt(plain_text_literal)
            cipher_text = base64.b64encode(cipher)
            temp_Rijndael = temp_Rijndael + cipher_text.decode()
            # Running Two fish
            T = Twofish(key_literal)
            x = T.encrypt(plain_text_literal)
            cipher_text = base64.b64encode(x)
            temp_Twofish = temp_Twofish + cipher_text.decode()
        file_MARS = "MARS-cipher-" + str(i) + ".txt"
        file_Rijndael = "Rijndael-cipher-" + str(i) + ".txt"
        file_Twofish = "Twofish-cipher-" + str(i) + ".txt"
        file = open(file_MARS, "w+")
        file.write(temp_MARS)
        file.close()
        file = open(file_Rijndael, "w+")
        file.write(temp_Rijndael)
        file.close()
        file = open(file_Twofish, "w+")
        file.write(temp_Twofish)
        file.close()
    except:
        i = i + 1