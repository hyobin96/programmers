# 백트래킹 ? 백트래킹은 시간초과
# 열을 고정하고 행만 결정

def solution(n):
    def is_not_attack(r, c):
        for qr, qc in queen_rc:
            if r == qr or abs(r - qr) == abs(c - qc):
                return False
        return True
    
    def dfs(curr_r, queen_rc):
        nonlocal answer
        if len(queen_rc) == n:
            answer += 1
            return
        
        for r in range(n):
            if is_not_attack(r, len(queen_rc)):
                queen_rc.add((r, len(queen_rc)))
                dfs(r + 1, queen_rc)
                queen_rc.remove((r, len(queen_rc) - 1))
                    
    answer = 0
    queen_rc = set()
    dfs(0, queen_rc)
    
    return answer