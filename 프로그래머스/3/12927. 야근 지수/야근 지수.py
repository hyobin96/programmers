import heapq

def solution(n, works):
    pq = []
    for w in works:
        heapq.heappush(pq, -w)
        
    while n and pq:
        w = heapq.heappop(pq)
        if w == 0:
            continue
        w += 1
        n -= 1
        heapq.heappush(pq, w)
    
    total = 0
    while pq:
        total += heapq.heappop(pq) ** 2
        
    answer = total
    return answer