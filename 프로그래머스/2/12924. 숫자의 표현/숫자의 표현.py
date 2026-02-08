# 1 부터 n 까지의 합 = n * (n + 1) / 2
# a, b 까지의 합 = (a + b) * (b - a + 1) / 2
# 그냥 투포인터

def solution(n):
    left, right = 1, 1
    total = 1
    
    count = 0
    while right <= n:
        if total < n:
            right += 1
            total += right
        elif total >= n:
            if total == n:
                count += 1
            total -= left
            left += 1
            
    
    answer = count
    return answer