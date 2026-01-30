# 컬럼 8 이하, (8C1 + 8C2 + ... + 8C8) * 20
# 최소성 만족 -> 

from itertools import combinations

def solution(relation):
    def is_key(idxs: set):
        s = set()
        for row in relation:
            l = []
            for i in idxs:
                l.append(row[i])
            record = tuple(l)
            if record in s:
                return False
            s.add(record)
        return True
    
    def 최소성_만족(idxs):
        # print(idxs)
        for key in keys:
            flag = True # 최소성 불만족 플래그
            for k in key:
                if k not in idxs:    
                    flag = False # 최소성 만족
                    break
            if flag:
                return False
        return True
            
    
    keys = set()
    
    def combi(curr: int, idxs: set, n: int):
        # print(idxs, n)
        if len(idxs) == n:
            # print(idxs)
            if is_key(idxs) and 최소성_만족(idxs):
                # print(idxs)
                keys.add(tuple(idxs))
            return
            
        for i in range(curr, len(relation[0])):
            idxs.add(i)
            combi(i + 1, idxs, n)
            idxs.remove(i)
    
    for i in range(1, len(relation[0]) + 1):
        combi(0, set(), i)
    
    # print(keys)
    
    return len(keys)