import hashlib
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# print(h.digest())
# print(h.hexdigest())
h=hashlib.new("SHA256")
current_password="MyPassword123567"
h.update(current_password.encode())
password_hash=h.hexdigest()
print(password_hash)

user_input="MyPassword123567"
h=hashlib.new("SHA256")
h.update(user_input.encode())
input_hash=h.hexdigest()
print(input_hash)

print(input_hash==password_hash)


CORRECT_HASH="3aaeb5943675846be1a67ba8a7777be581b88b0177927c8cb4d152bc8c167e17"
with open("Everything-1.4.1.1028.x86-Setup.exe","rb") as f:
    file_bytes=f.read()
    h=hashlib.sha256()
    h.update(file_bytes)
    file_hash=h.hexdigest()

print(file_hash==CORRECT_HASH)
digest=hashlib.file_digest(f)