#recursion algorithm
def mystery(n):
    if n > 0:
        mystery(n-2)
    print(n)

mystery(4)


#iterative algorithm
def mystery(n):
    k = 0
    while k <= n:
        print(k)
        k += 2
    else:
        return n
print(mystery(4))
