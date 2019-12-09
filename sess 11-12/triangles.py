def triangle(a,b,c):
    if a>=b and a>=c:
        max=a
        min1=b
        min2=c
    elif b>=a and b>=c:
        max=b
        min1=a
        min2=c
    else:
        max=c
        min1=a
        min2=b
    if min1+min2>max:
        print"we can make a triangle"
    else:
        print("wa cant make a triangle")
        return
    if min1==min2==max:
        print("Equilaterus")
    elif min1==min2 or min2==max or min1==max:
        print("isosceles")
    else:
        print("scalene")
    if max*max==(min1*min1)+(min2*min2):
        print("Rectanlgle")
    elif max * max > (min1 * min1) + (min2 * min2):
        print("obtuse")
    else:
        print("acute")

