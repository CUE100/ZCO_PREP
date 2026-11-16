P = [0]

for x in A:
    P.append(P[-1]+x)

P[right] - P[left-1]