#-*- coding:utf-8 -*-


import random
import string

print(random.randrange(100))

print("")

print(random.randrange(0,1000))

print("")

print(random.randrange (5,5000,5))

print("")

print(random.randrange(-9999,0))

print("")

def randomString(stringLength=10):
    """Gere uma string aleatória de tamanho fixo"""
    letters = (string.ascii_lowercase + string.ascii_uppercase + string.digits 
               + string.punctuation)
    return ''.join(random.choice(letters) for i in range(stringLength))


print ("A Senha Gerada é: ", randomString(30) )