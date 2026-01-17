# 미리 합을 계산

def solution(elements):
    s = set(elements)
    n = len(elements)
    
    elements += elements

    prefix_sum = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + elements[i - 1]
        
    # print(prefix_sum)
    for i in range(2, n + 1):
        for j in range(i, n + i):
            total = prefix_sum[j] - prefix_sum[j - i]
            s.add(total)
        

    return len(s)