# bfs
# 16 -> 1, 2 -> 
from collections import deque

def solution(storey):
    def mod10(n):
        while n % 10 == 0:
            n //= 10
        return n
        
    q = deque([(storey, 0)])
    answer = 2e8
    
    while q:
        floor, cnt = q.popleft()
        if floor < 10:
            # print(floor, cnt)
            answer = min(answer, cnt + floor, cnt + 10 - floor + 1)
            continue
        
        floor = mod10(floor)
        
        remain = floor % 10
        
        n_floor1 = (floor - remain)
        n_floor1 = mod10(n_floor1)    

        cnt1 = cnt + remain
        # print(n_floor1, cnt1)
        q.append((n_floor1, cnt1))


        n_floor2 = floor // 10 + 1
        n_floor2 = mod10(n_floor2)
        cnt2 = cnt + 10 - remain
        q.append((n_floor2, cnt2))

    return answer