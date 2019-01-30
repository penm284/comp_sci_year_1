import random
arr = [[random.randint(0,100) for col in range(10)] for row in range(10)]
length= len(arr)
first = arr[0][0]
middle = arr[length//2][length//2]
