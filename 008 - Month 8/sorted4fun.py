
def bubbly(arr):
    n = len(arr)
    for i in range(n):
        a = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                a = True
        if (a == False):
            break






if __name__ == '__main__':
    arr = [23, 10, 40, 120, 50 ,10 ,20 , 40]
    bubbly(arr)
    print("Sort Array")
    for i in range(len(arr)):
        print("%d" % arr[i], end =" ")
