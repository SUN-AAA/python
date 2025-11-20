import random

lst = set()
while True:
    c = random.randint(1,20)
    if c not in lst:
        lst.add(c)
    if len(lst) == 10:
        break

print(lst)

lst2 = []
while True:
    c2 = random.randint(1,20)
    if lst2.count(c2) == 0:
        lst2.append(c2)
    if len(lst2) == 10:
        break

print(lst2)