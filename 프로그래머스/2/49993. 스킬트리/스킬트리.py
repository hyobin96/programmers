def solution(skill, skill_trees):
    def is_possible(skill1, skill2):
        for s1, s2 in zip(skill1, skill2):
            if s1 != s2:
                return False
        return True
    
    d = dict()
    for i, s in enumerate(skill):
        d[s] = i
    
    answer = 0
    for s_t in skill_trees:
        l = []
        for s in s_t:
            if s in d:
                l.append(s)
        if is_possible(skill, l):
            answer += 1
        
        
    return answer