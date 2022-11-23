def find_min_value(arr):
    min_number = arr[0]
    for ele in arr:
        if min_number > ele:
            min_number = ele
    return min_number
    print(ele)

array = [0,4,5,-1,-2,3,6,8,12,32,45]    
find_min_value(array)