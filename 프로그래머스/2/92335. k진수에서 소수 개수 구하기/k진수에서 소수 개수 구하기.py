# k로 나누면서 소수 체크
# 문자열로 붙이기
# 0이 나오면 초기화

import math

def solution(n, k):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    
    answer = 0
    number = ''
    while n != 0:
        remain = n % k
        n //= k
        if remain == 0:
            if number and is_prime(int(number)):
                answer += 1
            number = ''
        else:
            number = str(remain) + number
            
    if number and is_prime(int(number)):
        answer += 1
    
    return answer
