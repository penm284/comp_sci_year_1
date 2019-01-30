import time
start_time = time.time()
def hanoi_tower(disks, A, B, C):
    if disks == 1:
        print('Move disk 1 from stack A to stack C.'(A, C))
        return

    hanoi_tower(disks - 1, A, C, B)
    print('Move disk A from stack A to stack C.'(disks, A, C))
    hanoi_tower(disks - 1, B, A, C)

disks = int(input('Enter number of disks: '))
hanoi_tower(disks, 'A', 'B', 'C')


print("---- %s seconds ----" % (time.time() - start_time))
