#Write an insertion sort

array = [458, 215, 287, 285, 459, 408, 171, 221, 186, 108, 81, 121, 264, 281, 494, 299, 403, 222, 401, 184, 307, 227, 150, 361, 274, 323, 479, 456, 430, 18, 343, 437, 265, 140, 460, 72, 331, 370, 316, 375, 57, 196, 204]
boundary = len(array)
for i in range(1, boundary, 1):
    temp = array[i] # Make the current term temporary
    count = i #Value to check all the indexes before it
    while count > 0 and array[count-1] > temp: #Check if current position is correct
        array[count] = array[count-1] #Shift previous term up
        count = count -1 #Moves to nect term behind
    array[count] = temp #Place term in right place

print(array)
