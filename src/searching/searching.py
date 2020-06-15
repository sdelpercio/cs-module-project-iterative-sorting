def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    elif len(arr) > 2:
        middle = (len(arr)- 1) // 2
    else:
        middle = 1
        
    if arr[middle] == target:
        return middle
    elif target > arr[middle]:
        return binary_search(arr[middle:], target)
    else:
        return binary_search(arr[:middle], target)


    return -1  # not found
