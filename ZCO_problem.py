def zco_prob(arr, K):
    arr.sort()
    n = len(arr)
    count = 0
    p = 0
    for i in range(n):
        while p < n and arr[p] - arr[i] < K:
            p += 1
        count += n - p
    return count