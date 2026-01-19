# map
# wants = map
# 

def solution(want, number, discount):
    d = dict()
    for i, w in enumerate(want):
        d[w] = i
    
    n = 10
        
    counts = [0] * len(number)
    for i in range(n):
        w = discount[i]
        if w in d:
            counts[d[w]] += 1
    
    answer = 0
    if counts == number:
        answer += 1
        
    for i in range(n, len(discount)):
        curr = discount[i]
        prev = discount[i - n]
        if curr in d:
            counts[d[curr]] += 1
        if prev in d:
            counts[d[prev]] -= 1
        
        if number == counts:
            answer += 1
        
        
    return answer