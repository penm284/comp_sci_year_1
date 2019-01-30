import time
start_time = time.time()

memo = {}
def trib(n):
    if n in memo
        return memo[n]

    if ( n<= 1)
        return n

    else:
        t = trib(n-1) + trib(n-2) + trib(n-3)

print("---- %s seconds ----" % (time.time() - start_time))


#1168
import timeit
start_time = time.clock()
memo = {}
def fib(n):
    if n in memo:
        return memo[n]

    if (n <= 1):
        return n

    else:
        f = fib(n - 1) + fib(n - 2)

    memo[n] = f
    return f

for n in range(1,1000):
    print(n, ":", fib(n))
print(timeit.default_timer() - start_time, "seconds")
print(fib(100))
