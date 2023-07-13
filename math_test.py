import math 
import random

result1 = math.pow(2,4)
print("result1 is", result1)

result2 = math.sqrt(16)
print("result2 is", result2)

result3 = random.randint(0, 100)
print("result3 is", result3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names: ", names)

random.shuffle(names)
print("Names after shuffling: ", names)

result4 = random.choice(names)
print("Chosen name is: ", result4)