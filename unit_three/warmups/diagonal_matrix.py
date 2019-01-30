matrix = [[0 + x for x in range(5)] for y in range(5)]


# add all the columns and find column with highest sum
totals = []
for col in range(len(matrix)):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][col]
    totals.append(total)
highest_val = max(totals)
print(highest_val)


#diagonal sum of a matrix
total = 0
for row in range(len(matrix)):
    total += matrix[row][row]
print(total)

#diagonal sum of matrix from the bottom right
total = 0
row = 5
for col in range(len(matrix)):
    row -= 1
    total += matrix[row][col]
print(total)
