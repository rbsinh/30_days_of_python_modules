from cryptography.fernet import Fernet,MultiFernet
key=Fernet.generate_key()
f=Fernet(key)
message=b'ASA Learning'
fernettoken=f.encrypt(message)
print(fernettoken)
decryptmessage=f.decrypt(fernettoken)
print(decryptmessage)
decryptmessage.decode('utf-8')
print(decryptmessage)


key1=Fernet(Fernet.generate_key())
key2=Fernet(Fernet.generate_key())
multifer= MultiFernet([key1,key2])
message=b'Explained in minutes'

fernettoken=multifer.encrypt(message)
print(fernettoken)
# multifer.decrypt(fernettoken.decode('utf-8'))

print(multifer.decrypt(fernettoken).decode('utf-8'))



import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend



password = b'123456'

# Print the random bytes string 
# Output will be different everytime
salt = os.urandom(16)
print(salt)

# Key derivation funtion - cryptographic hash function 
# Password Based Key Derivation Function 2 hash-based message authentication code
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
# key=kdf.derive(password)
# kdf.verify(password,key)



key = base64.urlsafe_b64encode(kdf.derive(b'password1234'))
f = Fernet(key)



message = b'Subscribe to ASA Learning'



# Encrypt the message
# The result of this encryption is known as a "Fernet token"
fernettoken = f.encrypt(message)

print(fernettoken)


f.decrypt(fernettoken).decode('utf-8')
