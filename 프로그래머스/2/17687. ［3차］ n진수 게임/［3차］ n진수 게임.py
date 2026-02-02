# p + m * i마다 튜브 차례
# 진법 변환
# t개가 되면 break
import math

def solution(n, t, m, p):
    
    d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    
    def to_진수(n, number):
        result = ""
        if number == 0:
            result = "0"
        while number != 0:
            나머지 = number % n
            if 나머지 >= 10:
                나머지 = d[나머지]
            else:
                나머지 = str(나머지)
            result = 나머지 + result
            number //= n
        return result
    
    # for i in range(0, 10):
    #     print(to_진수(2, i))
    num = 0
    순서 = 1
    answer = []
    while t != 0:
        진수_숫자 = to_진수(n, num)
        for 숫자 in 진수_숫자:
            if 순서 == p:
                answer.append(숫자)
                p += m
                t -= 1
                if t == 0:
                    break
            순서 += 1
        num += 1
    
    return ''.join(answer)