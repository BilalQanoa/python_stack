import random


def randInt1 (min = 0, max = 100):
    for i in range(min, max):
        print(i)

randInt1(min=50, max=70)


def randInt(min= 0 , max= 100):
    num = random.randint(min, max)
    return num

print(randInt())             # should print a random integer between 0 to 100
print(randInt(max=50))         # should print a random integer between 0 to 50
print(randInt(min=50))         # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500