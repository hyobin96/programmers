from collections import deque

def solution(s):
    q = deque()
    for string in s:
        if not q:
            q.append(string)
        elif q and q[-1] == string:
            q.pop()
        else:
            q.append(string)
    answer = 0 if q else 1
    return answer