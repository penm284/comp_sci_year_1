import time
start_time = time.clock()

#Iterative fibonacci search:
def fib(n):
    count = 0
    n_1 = 0
    n_2 = 1
    while count <= n/2:
        n_1 = n_1 + n_2
        n_2 = n_1 + n_2
        count = count + 1
    print(n_1)
fib(1000000)

print("---- %s seconds ----" % (time.clock() - start_time))



#Recursion(divide and conquer with memoization):
memo = {}
def fib(n):
    if n <= 1:
        return n
    elif n is in memo:
        return memo[n]
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f
fib(100)
