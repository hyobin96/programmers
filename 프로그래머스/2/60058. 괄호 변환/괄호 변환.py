# u는 균형잡힌 괄호 문자열로는 더 이상 분리할 수 없어야 함
# 그 경우는 () , )(, ))(( (()), (()))(
# 한 마디로 짝이 맞으면 된다? 짝이 맞는 순간 u

def solution(p):
    d = {"(": 1, ")":-1}
    
    def is_올바른(u):
        cnt = 0
        for s in u:
            cnt += d[s]
            if cnt < 0:
                return False
        return True
    
    def remove_reverse(u):
        if len(u) == 2:
            return ""
        u = u[1:-1]
        l = []
        for s in u:
            if s == "(":
                l.append(")")
            else:
                l.append("(")
        return ''.join(l)
            
    
    def recur(w):
        if w == "":
            return ""
        
        u, v = 0, 0
        cnt = 0
        for i in range(len(w)):
            cnt += d[w[i]]
            if cnt == 0:
                u = w[ : i + 1]
                v = w[i + 1 : ]
                break
        if is_올바른(u):
            u += recur(v)
            return u
        s = ""
        s += "(" + recur(v) + ")" + remove_reverse(u)
        return s
    
    return recur(p)
    
