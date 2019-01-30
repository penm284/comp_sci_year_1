import random

matrix = [[0 + x for x in range(7)]for y in range(8)]
#print(passengers)



#print(passengers[0][0])
#print(passengers[1][0])

#for x in range(0,8):
#    passengers[x][0] = daily_riders[x]
#print(passengers)


def d_total(col, matrix):
    ans = 0
    for num in range(len(matrix)):
        ans += matrix[num][col]
    return ans

print(d_total(3, matrix))


# row for loop
# col for loop
# find correct col
# add num to sum
# return sum
