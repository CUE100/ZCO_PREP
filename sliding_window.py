def sliding_window(A,K):
    best = 0

    for i in range(len(A)):

        length = A[i] - A[i-1]

        if length < best or best == 0:
            length = best
        return best