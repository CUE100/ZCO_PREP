events = (1,2), (3,4), (0,6), (5,7), (8,9), (5,9)

def greedy(events):
    pairs = []
    for start,end in events:
        pairs.append((end,start))
    pairs.sort()

    total = 0
    largest_end = 0

    for end, start in pairs:
        if start >= largest_end:
            largest_end = end
            total += 1
    return total

greedy(events)