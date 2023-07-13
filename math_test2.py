import math as m
import random as rand

result1 = m.pow(2,4)
print("result1 is", result1)

result2 = m.sqrt(16)
print("result2 is", result2)

result3 = rand.randint(0, 100)
print("result3 is", result3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names: ", names)

rand.shuffle(names)
print("Names after shuffling: ", names)

result4 = rand.choice(names)
print("Chosen name is: ", result4)