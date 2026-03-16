def solution(routes):
    routes.sort()
    
    i, j = 0, 0
    s1, e1 = routes[0]
    cnt = 0
    while j < len(routes):
        s2, e2 = routes[j]
        if e1 < s2:
            cnt += 1
            i, j = j, j + 1
            e1 = e2
        else:
            e1 = min(e1, e2)
            j += 1
    
    answer = cnt + 1
    return answer