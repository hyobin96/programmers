# 보조 컨테이너 벨트 = 스택
# q에 1 ~ len(order) 넣기
# q에서 하나씩 꺼내면서 order를 만족하는지 확인
# q에서 꺼낸 것과 stack의 제일 위 둘 중에 있다면 꺼내고 싣기
# 둘 중에 없다면 stack에 넣기
# q에서 다꺼냈는데 stack 제일 위에도 없다면?
# 끝

from collections import deque

def solution(order):
    q = deque([i for i in range(1, len(order) + 1)])
    s = []
    
    i = 0
    answer = 0
    while q:
        o = order[i]
        if q[0] == o:
            q.popleft()
            answer += 1
            i += 1
        elif s and s[-1] == o:
            s.pop()
            answer += 1
            i += 1
        else:
            s.append(q.popleft())
        
    while s and s[-1] == order[i]:
        s.pop()
        answer += 1
        i += 1
    
    return answer