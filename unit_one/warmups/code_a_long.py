arr = {'Dunca', 'Tequila', 'Mara', 'Bibsy', 'Stephane'}

print(arr{-1})

print("I am the last element" , arr{-1})

print("I am the first element" , arr{0})
#get len of array
print("I have", len(arr), "elements in me")
# pop to remove last element
arr.pop(
print(arr)
#remove a certain element
arr.remove('Mara')
print(arr)
#add something to array

arr.append('Woof')
print(arr)

# for loop
for name in arr:
    print(name)

#while loop
count=0
while len(arr) < count:
    print(count)
    count = count + 1
