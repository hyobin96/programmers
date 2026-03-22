# 9 11 14 10 

def solution(sticker):
    n = len(sticker)
    sticker = [0] + sticker
    dp1 = [0] * (n + 1)
    dp1[1] = sticker[1]
    dp2 = [0] * (n + 1)
    
    for i in range(2, n):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 3] + sticker[i])
    for i in range(2, n + 1):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 3] + sticker[i])
    
    max_total = max(max(dp1), max(dp2))

    answer = max_total
    return answer