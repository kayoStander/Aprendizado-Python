import random

CAPS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
DOWN = 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower()
NUMS = '1234567890'


OPS = {'CAPS': True, 'DOWN': True, 'NUMS': True, 'LET': True}

passw = ''

if OPS['CAPS'] == True:
    passw += CAPS

if OPS['DOWN'] == True:
    passw += DOWN

if OPS['NUMS'] == True:
    passw += NUMS

length = 20
amount = 10

for i in range(amount):
    password = ''.join(random.sample(passw,length))
    print(password)

