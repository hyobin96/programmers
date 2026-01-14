# 배열에 기록
# 3, 2, 4, 2, 4, 3 경우
import sys

def solution(weights):
    l = [0] * 1001
    for w in weights:
        l[w] += 1
        
    answer = 0    
    for i in range(100, 1001):
        count = l[i]
        if not count:
            continue
        
        answer += count * (count - 1) // 2
        for dist in (3, 4):
            torque = i * dist
            for d in (2, 3):
                if dist == d:
                    continue
                if torque % d == 0:
                    y = torque // d
                    if 100 <= y <= 1000:
                        answer += l[i] * l[y]
                        # print(i, y)
        
    return answer