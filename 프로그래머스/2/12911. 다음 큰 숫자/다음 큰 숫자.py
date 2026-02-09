def solution(n):
    count = format(n, 'b').count('1')
    
    while True:
        n += 1
        n_binary = format(n, 'b')
        
        if n_binary.count('1') == count:
            break
    
    
    answer = n
    return answer