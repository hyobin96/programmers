# h / w 는 열당 h / w 만큼 차지한다는 의미
# h / w 만큼 올라가다가 열을 못넘어가면?
# 5 / 3    10 / 3   15 / 3

import math

def solution(w,h):
    answer = w * h
    if w > h:
        w, h = h, w
        
    나머지 = h % w
    정수, 분자, 분모 = h // w, 나머지, w
    cnt = 0
    for _ in range(w):
        cnt += 정수
        if 분자:
            cnt += 1
        분자 += 나머지
        if 분자 >= w:
            cnt += 1
            분자 %= w
            
            
    return answer - cnt