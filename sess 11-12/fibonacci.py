def rec_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return rec_fib(n-2)+rec_fib(n-1)
n=int(input("Write number"))
print rec_fib(n)