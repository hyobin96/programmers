# k = 1 이고 d 가 1_000_000 이면 
# 원을 그려야 한다?
# 상단에서 오른쪽 아래로 이동하면서 d가 넘는지 확인, d가 넘으면 아래로 넘지 않으면 오른쪽으로
# 넘지 않으면 y // k + 1개 , y가 0보다 작으면 return  

def solution(k, d):
    dist_square = d * d
    
    answer = 0
    
    # 0, d -> d, 0
    x, y = 0, d
    while y >= 0:
        if x * x + y * y <= dist_square:
            answer += y // k + 1
            x += k
        else:
            y -= 1
    
    return answer
    
    
    return answer