# 5개씩 잘라서 다이아로 캤을 때, 철로 캤을 때, 돌로 캤을 때를 계산
# 그럼 길이는 최대 10
# 완탐 10!? 백트래킹 잘 하면 적을 듯? 근데 d, iii, ss
# (다이아, 철, 돌) 피로도 (5, 17, 85), (3, 7, 31)
# (다이아, 철, 돌) 개수  (3, 2, 0), (1, 1, 1)
# 다이아, 철 개수 순으로 정렬

def solution(picks, minerals):
    
    def mineral_count(m, counts):
        if m == 'diamond':
            counts[0] += 1
        elif m == 'iron':
            counts[1] += 1
        else:
            counts[2] += 1
        
    n = sum(picks)
    
    minerals = [0] + minerals
    
    arr = []
    
    counts = [0] * 3
    for i in range(1, len(minerals)):
        m = minerals[i]
        mineral_count(m, counts)
        
        if i % 5 == 0:
            arr.append(counts)
            counts = [0] * 3
        
        if i // 5 == n:
            break
    
    if sum(counts) > 0:
        arr.append(counts)
        
    arr.sort(reverse=True)
    # print(arr)
    
    answer = 0
    for count in arr:
        if picks[0]:
            answer += sum(count)
            picks[0] -= 1
        elif picks[1]:
            answer += count[0] * 5 + count[1] + count[2]
            picks[1] -= 1
        else:
            answer += count[0] * 25 + count[1] * 5 + count[2]
            picks[2] -= 1
    
    return answer