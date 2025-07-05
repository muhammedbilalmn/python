def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1)+fib(n-2)


hash_map = {0:0,1:1}

def fib_dp(n):
    if n in hash_map:
        return hash_map[n]
    hash_map[n] = fib_dp(n-1) + fib_dp(n-2)
    return hash_map[n]

def new_dp(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a,b = 0,1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c
import datetime
start = datetime.datetime.now()

# print(fib_dp(300))
print(new_dp(1000))

end = datetime.datetime.now()
print(end-start)