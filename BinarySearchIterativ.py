def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while(low <= high):
        mid = (high + low // 2)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1
arr = [1,4,10,15,18,25,30]
x = int(input()) 
result = binary_search(arr, x)
if result!=1:
    print("Elementul se afla pe pozitia: ", str(result))
else: 
    print("Elementul nu se afla in vector ")      
