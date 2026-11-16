def smallest_gap(arr):
    arr.sort()
    best = arr[1] - arr[0]
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) < best:
            best = (arr[i+1] - arr[i])
    return best