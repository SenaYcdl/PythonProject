# Since the condition next to the while statement is true forever,
# our program will continue to run forever.
# These types of loops are called infinite loops.
# while True:
# print('I love You<3')


"""import time
counter=0
while counter>=0:
    counter+=1

    print(counter)
    time.sleep(1)"""

import random

while True :
    random_number=random.randrange(1000)
    print(random_number)

    if random_number == 777:
        print('Found!')
        break


names = ['Max', 'Felix', 'Nida', 'Lucas', 24, 'Sarah']

for name in names:
    if type(name) != str:
        print('Found', name)
        break

    else:
        print(name, 'is a string')


"""
Max is a string
Felix is a string
Nida is a string
Lucas is a string
Found 24
As you can see, when the type() 
function reaches 26, it recognizes 
that it is not a string type
 data and the loop will be stopped.
"""


i = 1
while True:
    print(i)
    i += 2
    if (i == 5):
        break

num2 = 3.4
if num2 > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")

x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)



