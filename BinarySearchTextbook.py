#Write a binary search

array = [1, 2, 4, 23, 47, 289, 467, 692, 903, 1036, 1837, 3522, 4008, 5621, 5877, 7299, 9091]

find = int(input("Value to search"))
last = len(array)-1
first = 0
flag = False

while first <= last and flag == False:
    mid = int((first + last)/2)
    if array[mid] == find:
        flag = True
    elif array[mid] < find:
        first = mid + 1
    else:
        last = mid -1

if flag == False:
    print("Not found")
if flag == True:
    print("Found in location", mid)
