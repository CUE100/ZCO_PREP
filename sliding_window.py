def sliding_window(A,K):
    best = 0
    left= 0
    window_sum = 0

    for i in range(len(A)):
        window_sum += A[i]
        while window_sum > K:
            window_sum -= A[left]
            left += 1
        if window_sum == K:
            length = i - left +1
            if length < best:
                best = length 
    return best
        