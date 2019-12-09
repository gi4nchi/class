def f(list):
    m=list[0]
    for i in list:
        if i>n:
            n=i
    return n

import random
number_list=[]
for i in range(4):
    number_list.add(random.random(-1000,1000))
a=f(number_list)
print(a)
