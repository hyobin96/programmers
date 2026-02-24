def solution(str1, str2):
    def get_union_count(d1, d2):
        count = 0
        for k, v in d1.items():
            count += max(v, d2.get(k, 0))
        for k, v in d2.items():
            if k not in d1:
                count += v
        return count
    
    def get_intersect_count(d1, d2):
        count = 0
        for k, v in d1.items():
            count += min(v, d2.get(k, 0))
        return count
        
    d1, d2 = dict(), dict()
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1) - 1):
        s1, s2 = str1[i], str1[i + 1]
        if 'a' <= s1 <= 'z' and 'a' <= s2 <= 'z':
            s = s1 + s2
            d1[s] = d1.get(s, 0) + 1
    
    for i in range(len(str2) - 1):
        s1, s2 = str2[i], str2[i + 1]
        if 'a' <= s1 <= 'z' and 'a' <= s2 <= 'z':
            s = s1 + s2
            d2[s] = d2.get(s, 0) + 1
                
    분모 = get_union_count(d1, d2)
    분자 = get_intersect_count(d1, d2)
    
    answer = int((분자 / 분모) * 65536) if 분모 != 0 else 65536
    return answer