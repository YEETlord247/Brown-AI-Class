from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice

result1 = pow(2,4)
print("result1 is", result1)

result2 = sqrt(16)
print("result2 is", result2)

result3 = randint(0, 100)
print("result3 is", result3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names: ", names)

shuffle(names)
print("Names after shuffling: ", names)

result4 = choice(names)
print("Chosen name is: ", result4)