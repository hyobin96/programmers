# 길을 지나갔는지 나타내는 배열
# 3차원?
# [0][0][0 ~ 3]
# road[10][10]

def solution(dirs):
    # 상 좌 하 우
    drs, dcs = (-1, 0, 1, 0), (0, -1, 0, 1)
    dir = {'U': 0, 'L': 1, 'D': 2, 'R': 3}
    
    road = [[[0] * 4 for _ in range(11)] for _ in range(11)]
    
    in_range = lambda r, c: 0 <= r < 11 and 0 <= c < 11
    
    dist = 0
    r, c = 5, 5
    for d in dirs:
        d = dir[d]
        nr, nc = r + drs[d], c + dcs[d]
        if not in_range(nr, nc):
            continue
        
        if not road[r][c][d] and not road[nr][nc][(d + 2) % 4]:
            dist += 1
        road[r][c][d], road[nr][nc][(d + 2) % 4] = 1, 1
        r, c = nr, nc
        
    
    return dist