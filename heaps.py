import heapq

def heaps(ropes):
    
    heapq.heapify(ropes)
    total = 0
    while len(ropes) > 1:
        a = heapq.heappop(ropes)
        b = heapq.heappop(ropes)

        total += a+b
        heapq.heappush(ropes, a + b)
    return total #important for zco exam
