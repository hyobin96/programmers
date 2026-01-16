# 공약수를 구해서
# A 에서 공약수 구하는 방법은 gcd 이용, 최대공약수
# 최대공약수보다 작은 약수가 상대방의 조건을 만족한다면?
# 12, 24 -> 2, 3, 4, 6, 12   인 경우 3, 5 면 12
# 애초에 최대공약수는 만족하지 않으면서 최대공약수의 약수를 만족하는 경우?
# 12 -> a * b * c ... 최대공약수로 나누어 진다는 말은 a * b * c * ... 라는 이야기
# 따라서 최대공약수의 약수인 b, c 로 반드시 나누어진다
# 따라서 최대공약수보다 작은 약수가 만족하는 경우는 없다

import math

def solution(arrayA, arrayB):
    def get_gcd(array):
        gcd = array[0]
        for i in range(1, len(array)):
            gcd = math.gcd(gcd, array[i])
            if gcd == 1:
                gcd = 0
                break
                
        return gcd
    
    def is_possible(gcd, array):
        for num in array:
            if num % gcd == 0:
                return False
        return True
    
    gcd1 = get_gcd(arrayA)
    gcd2 = get_gcd(arrayB)
    
    answer = 0
    if gcd1:
        answer = max(answer, gcd1 if is_possible(gcd1, arrayB) else 0)
    if gcd2:
        answer = max(answer, gcd2 if is_possible(gcd2, arrayA) else 0)

    return answer