# 등장하는 횟수는 약수의 개수
# 약수의 개수를 구하는 방법? sqrt? -> logn, log5e6 * 5e6
# 1에서 e까지 모두 약수 개수 구해놓기
# 그다음 i부터 e까지 가장 많은 약수 개수를 가지는 배열[i] 만들기
# 그럼 정답은 배열[i]

def solution(e, starts):
    pre_약수_counts = [1] * (e + 1)
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            pre_약수_counts[j] += 1
    
    pre_max_number = [0] * (e + 1)
    pre_max_number[e] = e
    for i in range(e - 1, 0, -1):
        prev = pre_max_number[i + 1]
        if pre_약수_counts[i] >= pre_약수_counts[prev]:
            pre_max_number[i] = i
        else:
            pre_max_number[i] = prev
    # print(pre_max_number)
    result = []
    for s in starts:
        result.append(pre_max_number[s])
        
    answer = result
    return answer