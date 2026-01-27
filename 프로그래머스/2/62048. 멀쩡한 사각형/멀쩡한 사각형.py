import math

def solution(w,h):
    answer = w * h
    if w > h:
        w, h = h, w
        
    나머지 = h % w
    정수, 분자, 분모 = h // w, 나머지, w
    cnt = 정수 * w
    cnt2 = 0
    for _ in range(w):
        if 분자:
            cnt2 += 1
        분자 += 나머지
        if 분자 >= w:
            cnt2 += 1
            분자 %= w
            
            
    return answer - cnt - cnt2