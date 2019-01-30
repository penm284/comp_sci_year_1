def fib(num):
    count = 0
    num_1 = 0
    num_2 = 1
    while count <= num/2:
        num_1 = num_1 + num_2
        num_2 = num_1 + num_2
        count = count + 1
    print(num_1)
fib(100)
