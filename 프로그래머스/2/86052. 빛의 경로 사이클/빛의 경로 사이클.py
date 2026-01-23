# L R 은 방향 기억해서 if 문 관리
# 그럼 사이클인지 아닌지는 어떻게 알지?
# 시작과 똑같아지면 사이클
# 시작을 기록
# 모든 문자열에 기록 필요
# hash 이용, (들어가는 방향, 들어가는 문자열의 위치)
# 방향 = (-1, 0), (0, -1), (1, 0), (0, 1)
# 문자열 위치 = (i, j)
# 방향 전환 판별함수 필요

def solution(grid):
    drs, dcs = (-1, 0, 1, 0), (0, -1, 0, 1)
    
    def switch_direction(d, s):
        # -1 0 -> 0, -1, 1, 0 -> 0, 1, 0, -1 -> 1, 0, 0, 1 -> -1, 0
        if s == 'L':
            d = (d + 1) % 4
        # -1, 0 -> 0, 1, 0, -1 -> -1, 0
        elif s == 'R':
            d = (d + 3) % 4
        return d
            
    def next_to_grid(i, j):
        if i < 0:
            i = n - 1
        if i >= n:
            i = 0
        if j < 0:
            j = m - 1
        if j >= m:
            j = 0
        return (i, j)
        
    def get_cycle_length(c_h):
        nonlocal cycle_hashs
        d, i, j = c_h
        dist = 0
        while c_h not in cycle_hashs:
            cycle_hashs.add(c_h)
            dist += 1
            d = switch_direction(d, grid[i][j])
            i, j = i + drs[d], j + dcs[d]
            i, j = next_to_grid(i, j)
            c_h = (d, i, j)
        return dist
    
    cycle_hashs = set()
    answer = []
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            for d in range(4):
                c_h = (d, i, j)
                if c_h not in cycle_hashs:
                    dist = get_cycle_length(c_h)
                    answer.append(dist)
    answer.sort()
    
    return answer