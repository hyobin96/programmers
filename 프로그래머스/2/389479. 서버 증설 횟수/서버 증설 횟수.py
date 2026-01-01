from collections import deque

def solution(players, m, k):
    
    server_nums = 0
    count = 0
    q = deque() # (시각, 증설한 서버의 수)
    
    for i, p in enumerate(players):
        if q and i - q[0][0] == k:
            server_nums -= q[0][1]
            q.popleft()
            
        server_nums
        request_server_nums = p // m
        offset = request_server_nums - server_nums
        if offset > 0:
            q.append((i, offset))
            count += offset
            server_nums += offset
            
    
    return count