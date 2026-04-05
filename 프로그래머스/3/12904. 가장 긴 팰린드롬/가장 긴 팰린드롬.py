def solution(s):
    s = '#' + '#'.join(s) + '#'
    s_length = len(s)
    A = [0] * s_length
    
    for i in range(s_length):
        A[i] = 0
        
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < s_length and s[i - A[i] - 1] == s[i + A[i] + 1]:
            A[i] += 1
        
    
    max_length = max(A)
    answer = max_length
    return answer