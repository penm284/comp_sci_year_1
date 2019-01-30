arr1 = [1,7,8,3,5,87,95,38,94,65,77,356,94,35,23,12,34,53,67,2,6,2,7,5,3,7,2,8,2,4,6,3,73,53,57,74,27,83,765]

new_arr = []
while arr1:
    minimum = arr1[0]#set first index value to minimum

    for val in arr1:#compare the saved val to the previous val
        if val < minimum:#cycle through each arr val and compare to the previous following values
            minimum = val

    new_arr.append(minimum)#add the lowest saved number to the new arr in increasing order
    arr1.remove(minimum)#remove the number from the old arr

print(new_arr)
