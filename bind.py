


def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x: 
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1




# initialization of main

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,10,20,30,40,50,60]
    x = 50
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print(result)
    else:
        exit(1)
