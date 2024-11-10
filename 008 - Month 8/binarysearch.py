
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

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("The element in your array is: ", result.value)
    else:
        print("You have no matching element in the array")
