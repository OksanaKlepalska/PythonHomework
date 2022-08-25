import random

def my_random(a, b):
    l=[]
    for i in range(random.randint(0, b)):
        l.append(random.randint(0, 9))
    print(l)


my_random(12, 17)