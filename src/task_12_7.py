import random
import re



psw =''
for i in range(12):
    psw += chr(random.randint(33,122))

print(psw)
