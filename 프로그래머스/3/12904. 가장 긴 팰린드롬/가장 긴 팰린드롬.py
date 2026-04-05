def solution(s):
    s = '#' + '#'.join(s) + '#'
    s_length = len(s)
    A = [0] * s_length
    
    r, center = -1, -1
    for i in range(s_length):
        if r >= i:
            A[i] = min(A[center - (i - center)], r - i)
        
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < s_length and s[i - A[i] - 1] == s[i + A[i] + 1]:
            A[i] += 1

        if i + A[i] > r:
            r, center = i + A[i], i
            
    
    max_length = max(A)
    answer = max_length
    return answer