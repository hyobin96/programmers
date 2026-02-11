# dp1, dp2로 쪼개기
# 홀수는 불가능
# dp2는 2개 마다 2개의 새로운 꼴이 등장


def solution(n):
    dp1 = [0] * (n + 4)
    dp2 = [0] * (n + 6)
    dp1[2] = 3
    dp2[4] = 2
    
    for i in range(4, n + 1, 2):
        dp2[i] = 2
        for j in range(i, 0, -1):
            dp1[i] += dp1[j] * dp2[i - j]
        
        dp1[i] = (dp1[i] + dp1[i - 2] * 3 + dp2[i]) % 1_000_000_007
    
    answer = dp1[n]
    return answer