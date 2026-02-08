# 1000만부터 내려가기
# 수가 매우 크다면?
# 소수인지 판별해서 소수라면 1 그대로 두기
# 5000 * log(10억) + 5000 * 10 ** 7 시간초과
# 

import math

def solution(begin, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    MAX_NUMBER = 10_000_000
    
    blocks = [1] * (end - begin + 1)
    if begin == 1:
        blocks[0] = 0
    
    position = end
    for i in range(len(blocks) - 1, -1, -1):
        s, e = 2, int(math.sqrt(position)) + 1
        
        for j in range(s, e):
            if position % j == 0:
                block = position // j
                if block <= MAX_NUMBER:
                    blocks[i] = block
                    break
                else: 
                    blocks[i] = max(blocks[i], j)
        position -= 1
    
    answer = blocks
    return answer