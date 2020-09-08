#a
from itertools import count
for el in count(3):
    if el > 9:
        break
    else:el+=1
    print(el)
#b
from itertools import cycle
num = 0
for el in cycle("WORLD"):
    if num > 20:
        break
    else:num+=1
    print(el)
