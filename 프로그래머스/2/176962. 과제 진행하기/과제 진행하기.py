# 스택
# 마지막에 취소한 거 리스트 끝에 추가
# [과목, 시작 시간, 남은 시간]
from collections import deque

def solution(plans):
    def get_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    for i, p in enumerate(plans):
        plans[i][1] = get_minutes(plans[i][1])
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x : x[1])
    q = deque(plans)
    
    stack = []
    t = q[0][1]
    result = []
    while q:       
        if not stack or (q and t == q[0][1]):
            p = q.popleft()
            if not q:
                result.append(p[0])
                break
            else:
                if p[1] + p[2] <= q[0][1]:
                    t = p[1] + p[2]
                    result.append(p[0])
                else:
                    t = q[0][1]
                    p[2] = p[2] - (q[0][1] - p[1])
                    stack.append(p)
        
        if stack:
            if q and t < q[0][1]:
                p = stack[-1]
                if p[2] <= q[0][1] - t:
                    t += p[2]
                    stack.pop()
                    result.append(p[0])
                else:
                    p[2] -= q[0][1] - t
                    t = q[0][1]
            elif not q:
                result.append(stack.pop()[0])
                
    while stack:
        result.append(stack.pop()[0])
            
    return result