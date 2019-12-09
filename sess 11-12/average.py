def avg(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
numbers=[]
i=0
while (i<4):
    try:
        n= input("Input a number")
        n=int(n)
        numbers.append(n)
        i+=1
    except:
        print("please enter a number")
