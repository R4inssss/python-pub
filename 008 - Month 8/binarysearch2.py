#!python3
# Second version of binary search

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2 # Discarding our remainder

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1




if __name__ == '__main__':
    arr = [1,2,3,4,10,30,40]
    x = 10
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print(result)
    else:
        exit(1)
