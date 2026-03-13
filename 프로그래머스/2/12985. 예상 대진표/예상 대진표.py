from math import ceil

def solution(n,a,b):
    cnt = 0
    while a != b:
        a = ceil(a / 2)
        b = ceil(b / 2)
        cnt += 1
    
    answer = cnt

    return answer