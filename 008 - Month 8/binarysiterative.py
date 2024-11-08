import random as rand
def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        print(mid, "|", x, "|", low, "|", high)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1





if __name__ == '__main__':
    arr = [1,2,3,5,10,20,30,40,50,60]
    x = int(input(">>> "))
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("The element in your array is: ", result)
    else:
        print("No element in the array")








