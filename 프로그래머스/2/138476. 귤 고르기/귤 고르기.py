# 귤 갯수 세서 제일 많은거 순으로 내림차순 정렬   #

from collections import Counter

def solution(k, tangerine):
    d = Counter(tangerine)
    counts = sorted(d.values(), reverse=True)
    
    answer = 0
    for count in counts:
        k -= count
        answer += 1

        if k <= 0:
            break
    
    return answer