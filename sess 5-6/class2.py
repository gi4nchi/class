base=5
power=4
toadd=1
for i in range(power):
    sum=0
    for j in range(base):
        sum=sum+toadd
    toadd=sum
print(toadd)