# 10! * 10
# 중복조합

from itertools import combinations_with_replacement


def solution(n, info):
    def is_low_score_many(result):
        for i in range(10, -1, -1):
            if result[i] > answer[i]:
                return True
            elif result[i] == answer[i]:
                pass
            else:
                return False
        return False
    
    def get_diff(result):
        diff = 0
        for i in range(11):
            a, b = info[i], result[i]
            if a < b:
                diff += 10 - i
            elif a == 0 and b == 0:
                pass
            else:
                diff -= 10 - i
                
        return diff
    
    def make_result(re):
        result = [0] * 11
        for idx in re:
            result[10 - idx] += 1
        return result
    
    answer = [0] * 11
    max_diff = 0
    for re in combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n):
        result = make_result(re)
        diff = get_diff(result)
        if diff > max_diff:
            max_diff = diff
            answer = result
        
        elif max_diff != 0 and diff == max_diff and is_low_score_many(result):
            answer = result
            
            
    return answer if max_diff else [-1]