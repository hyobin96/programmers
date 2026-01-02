def solution(info, n, m):
    # 직관적으로 생각했을 때 B의 흔적 개수와 A의 흔적 개수의 차가 작은 것은 B대비 A가 많은 것.
    # 따라서 이부터 처리하는 게 합리적으로 보임.
    # B가 훔칠 수 있으면 훔치기 -> 훔칠 수 있다는 건 훔쳤을 때 총 흔적 개수가 m 보다 작아야 함.
    
    
    info.sort(key=lambda x: (x[1] - x[0]))
    # print(info)
    
    answer = 0
    for a, b in info:
        if m - b > 0:
            m -= b
            continue
        if n - a > 0:
            n -= a
            answer += a
            continue
        
        return -1
    
    return answer