# lcm이 3.9 버전부터 있음
# 여기 버전은 3.8임
# 두 수 사이의 최소공배수는 num1 * num2 / gcd
# 이걸 반복

from math import gcd

def solution(arr):
    최소공배수 = arr[0]
    for num in arr:
        최소공배수 = 최소공배수 * num // gcd(최소공배수, num)
    
    answer = 최소공배수
    return answer