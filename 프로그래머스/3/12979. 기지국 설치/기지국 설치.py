import math

def solution(n, stations, w):
    dist = 2 * w + 1
    cnt = 0
    prev, curr = 1, 1
    for station in stations:
        curr = station - w - 1
        gap = curr - prev + 1
        if gap > 0:
            cnt += math.ceil(gap / dist)
        prev = station + w + 1

    last_gap = n - prev + 1
    if last_gap > 0:
        cnt += math.ceil(last_gap / dist)
    
    answer = cnt
    return answer