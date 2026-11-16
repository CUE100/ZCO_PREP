def range_sums(A, queries):
    P = [0]
    for x in A:
        P.append(P[-1] + x) 
    answers = []
    for left,right in queries:
        answer = P[right] - P[left-1]
        answers.append(answer)
    return answers