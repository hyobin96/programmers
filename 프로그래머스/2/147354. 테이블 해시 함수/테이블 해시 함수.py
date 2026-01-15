# 정렬, nlogn
# S_i는 sum(i) % i
# S_row_gegin ~ S_row_end XOR 반복
# 딱히 어려울 게 없는 문제

def solution(data, col, row_begin, row_end):
    # col번째 오름차순, 0번째 내림차순
    data.sort(key=lambda d: (d[col - 1], -d[0]))
    
    # row_begin 부터 row_end
    answer = 0
    for i in range(row_begin - 1, row_end):
        S_i = 0
        for d in data[i]:
            S_i += d % (i + 1)
        answer ^= S_i
    
    return answer