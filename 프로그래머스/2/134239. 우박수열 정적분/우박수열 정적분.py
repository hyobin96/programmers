# 그냥 하라는 대로 하면 풀릴듯
# 정적분은 사다리꼴 너비 더하면 됨
# (y1 + y2) / 2
# 매번 더하면 시간초과 예상, 미리 합 계산 필요

def solution(k, ranges):
    y = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        y.append(k)
            
    # print(y)
    # prefix_sum[i] 는 i번째 점까지의 넓이
    n = len(y)
    prefix_sum = [0] * n
    for i in range(1, n):
        area = (y[i] + y[i - 1]) / 2
        prefix_sum[i] = prefix_sum[i - 1] + area
    
    # print(prefix_sum)
    
    result = []
    for a, b in ranges:
        area = -1
        b = n + b - 1
        if a <= b:
            area = prefix_sum[b if b < n else -1] - prefix_sum[a if a < n else -1]
        result.append(area)
    
    return result