# enroll과 referral로 트리를 만들고
# seller는 map으로 합쳐놓으면 될거같기도 한데 ...
# 문제는 절삭이 되냐 안되냐가 문제
# 합치면 안될텐데

def solution(enroll, referral, seller, amount):
    enroll_map = dict()
    n = len(enroll)
    for i, name in enumerate(enroll):
        enroll_map[name] = i
        
    # print(enroll_map)
    
    tree = [-1] * n # parent만 기록
     
    for i, p in enumerate(referral):
        if p == "-":
            continue
        idx = enroll_map[enroll[i]]
        tree[idx] = enroll_map[p]
        
    result = [0] * n
        
    for i, s in enumerate(seller):
        c = enroll_map[s]
        profit = amount[i] * 100
        while c != -1 and profit != 0:
            profit_10 = profit * 10 // 100
            result[c] += profit - profit_10
            profit = profit_10
            c = tree[c]
        
    
    answer = result
    return answer