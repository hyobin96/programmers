from math import gcd
from collections import deque

def solution(signals):
    def get_lcm(n1, n2):
        return n1 * n2 // gcd(n1, n2)  
        
    times = []
    for s in signals:
        times.append(sum(s))
    # print(times)
    lcm = times[0]
    for t in times:
        lcm = get_lcm(lcm, t)
        
    qs = []    
    for s in signals:
        q = deque()
        for i, t in enumerate(s):
            for _ in range(t):
                q.append(i)
        qs.append(q)
        
    result = -1
    for i in range(lcm):
        s = set()
        for q in qs:
            s.add(q[0])
            q.append(q.popleft())
        if len(s) == 1 and q[-1] == 1:
            result = i + 1
            break
            
        
    answer = result
    return answer