#import timeit
#start = timeit.default_timer()



#def find(arr, val):
#    count = 0
#    for num in arr:
#        count = count + 1
#        if num == val:
#            print(count)
#            print("-1")


#arr = [98, 19, 1, 46, 51, 33, 3, 33, 80, 40]

#find(arr, 50)


#stop = timeit.default_timer()









array = [1,2,3,4,5,6,7,8,9,10]

def binary_search(array, num):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if num == val:
            return True
        elif num > val:
            if lower == x:
                break
            lower = x
        elif num < val:
            upper = x
binary_search(array, 6)


#def b_search(arr, val):
#    mid = len(arr)//2

#    if val == arr[mid]:
#        return True

#    elif val < arr[mid]:
#        b_search(arr[:len(arr)//2], val)

#    else:
#        b_search(arr[len(arr)//2+1:], val)

#my_nums = list(range(2002,2019))
#target = 16

#print(b_search(my_nums, target))

#find(arr, 4):
#def find(arr, int):
#    if int > arr(len/2):
#        find(int, arr[len/2])
#find(arr, 4)
