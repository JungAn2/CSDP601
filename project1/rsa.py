import sympy # sympy is a Python library for symbolic mathematics
import random
import math

class rsa:
    def __init__(self):
        self.p = sympy.randprime(10**100, 10**150)
        self.q = sympy.randprime(10**100, 10**150)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.gete()
        self.d = self.getd()
        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)

    def gete(self):
        e = random.randint(10**10, self.phi)
        while math.gcd(e, self.phi) != 1:
            e = random.randint(10**10, self.phi)
        return e
    
    def getd(self):
        d = pow(self.e, -1, self.phi)
        return d
    
    def encrypt(self, message):
        ascii_message = [ord(char) for char in message]
        encrypted_message = [pow(char, self.e, self.n) for char in ascii_message]
        return encrypted_message
    
    def decrypt(self, message):
        decrypted_message = [pow(char, self.d, self.n) for char in message]
        ascii_message = [chr(char) for char in decrypted_message]
        return ''.join(ascii_message)