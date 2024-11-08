def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low ) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1



if __name__ == '__main__':
    arr = [1,2,3,4,10,20,30,40]
    x = 10
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element in array is: ", result)
    else:
        print("No element found for the array value")
    

