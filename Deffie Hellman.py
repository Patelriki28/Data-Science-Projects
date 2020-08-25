import random
import hashlib
import sys

g=23
p=199

a=random.randint(5, 100)

b=random.randint(20,150)

A = (g**a) % p
B = (g**b) % p

print('The shared value of g is : ',g)
print('The prime number value of p is: ',p )

print('\nThe priveate key for Alice is: ',a)
print('Alice value : ',A,' (g^a) mod p')


print('\nThe private key for Bob is: ',b)
print('Bob value : ',B,' (g^b) mod p')

print('\nAlice calculates:')
keyA=(B**a) % p
print('Key: ',keyA,' (B^a) mod p')
print('Key: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print('\nBob calculates:')
keyB=(A**b) % p
print('Key: ',keyB,' (A^b) mod p')
print('Key: ',hashlib.sha256(str(keyB).encode()).hexdigest())