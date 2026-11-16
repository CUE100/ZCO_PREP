def smallest_diff(arr):
    best = abs(arr[1]-arr[0])

    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) < best:
                best = abs(arr[i] - arr[j])

    return best 