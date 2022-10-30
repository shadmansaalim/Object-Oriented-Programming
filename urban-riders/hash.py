"""Encryption example"""
# Rtrams -> smart
# Splkiyoanr -> lion

import hashlib

email = 'coder@gmail.com'
pwd = 'abc123'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_hash)
