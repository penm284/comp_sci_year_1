import random
matrix = [[66, 64, 52, 61, 65, 23, 12, 38, 37, 1], [62, 59, 18, 44, 84, 87, 18, 94, 95, 80], [86, 21, 73, 17, 47, 54, 38, 35, 91, 60], [64, 27, 18, 63, 40, 99, 31, 18, 56, 6], [78, 30, 85, 63, 32, 60, 65, 67, 30, 60], [10, 52, 99, 4, 100, 48, 94, 37, 11, 50], [90, 4, 24, 22, 99, 32, 51, 51, 88, 28], [48, 19, 24, 35, 59, 16, 99, 80, 95, 28], [7, 13, 43, 31, 31, 4, 54, 94, 100, 34], [50, 85, 36, 23, 23, 70, 75, 56, 89, 9]]

def find_mean(matrix):
    value = 0
    count = 0
    for x in range (len(matrix)):
        for y in range (len(matrix)):
            value = value + matrix[x][y]
            count = count + 1
    mean = value//count
    return mean
print(find_mean(matrix))

arr = [random.randint(0,100) for x in range(10)]

def ur_bent_search(arr,int):
    ans = 'false'
    for num in arr:
        if num == int:
            ans = 'True'
    print(ans)

ur_bent_search(arr,100)
