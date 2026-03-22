# 12라면, 345, 444, 5 12 -> 2 2 2 2 4  
# n 3 , s 8 -> 332,
# s % n  == 0 -> s // n 을 n개
# s % n != 0 -> s // n 을 n - 1 개 + s % n

def solution(n, s):
    if s < n:
        return [-1]
    
    q, r = divmod(s, n)
    result = [q] * n
    for i in range(r):
        result[i] += 1
    
    
    answer = sorted(result)
    return answer