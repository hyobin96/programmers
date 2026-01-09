# 맵 ? 맵 사이즈 체크로 판단

def solution(topping):
    def add_map(d, value):
        if value in d:
            d[value] += 1
        else:
            d[value] = 1
            
    def remove_map(d, value):
        d[value] -= 1
        if d[value] == 0:
            del d[value]
    
    철수 = dict()
    동생 = dict()
    for t in topping:
        add_map(동생, t)
    
    answer = 0
    for t in topping:
        add_map(철수, t)
        remove_map(동생, t)
        if len(철수) == len(동생):
            answer += 1
        
    return answer