# 10C5 하면, 5개를 골랐을 때마다 5개의 조합을 구해야 한다... 그러면 6 * 6 * 6* 6* 6 * 6
# 2 ** 5 * 3 ** 5 = 64 * 243 * 3 = 36_000 * 252 = 얼마안하네? 뭐야
from itertools import combinations, product

def solution(dice):
    n = len(dice)
    selects = combinations(range(n), n // 2)
    
    def get_prefix_sum(arr):
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        return arr
    
    max_wins = 0
    result = []
    for select1 in selects:
        select2 = []
        s = set(select1)
        for i in range(n):
            if i not in s:
                select2.append(i)
        
        l1, l2 = [0] * 500, [0] * 500
        select1_set, select2_set = set(), set()
        for i, p in enumerate(product(range(6), repeat = n // 2)):
            total1 = 0
            total2 = 0
            for d1, d2, j in zip(select1, select2, p):
                total1 += dice[d1][j]
                total2 += dice[d2][j]
            l1[total1] += 1
            l2[total2] += 1
            select1_set.add(total1)
            select2_set.add(total2)
        
        l2 = get_prefix_sum(l2)
        
        wins = 0
        for s1 in select1_set:
            wins += l1[s1] * l2[s1 - 1]
            
        if wins > max_wins:
            max_wins = wins 
            result = list(select1)
            for i in range(len(result)):
                result[i] += 1
            # print(result)
    
    answer = result
    return answer