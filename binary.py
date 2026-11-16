arr = [2, 5, 8, 12, 17, 21, 29, 35, 41]
target = 29
low = arr[0]
high = arr[len(arr) - 1]
while low<high:
    mid = (low+high) // 2
    if arr[mid] == target:
        print('found it')

    elif arr[mid] < target:
        low = mid+1

    else:
        high = mid-1     # knxj