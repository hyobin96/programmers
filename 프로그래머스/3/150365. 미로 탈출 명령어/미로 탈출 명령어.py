# x, y의 차의 합과 k가 모두 홀수이거나 짝수여야 함
# d, l, r, u 가 알파벳 순
# 하 좌 우 상
# (1, 0, 0, -1), (0, -1, 1, 0)

def solution(n, m, x, y, r, c, k):
    def is_possible(x, y, r, c):
        return (abs(x - r) + abs(y - c)) <= k and (abs(x - r) + abs(y - c)) % 2 == k % 2
    
    if not is_possible(x, y, r, c):
        return "impossible"
    
    in_range = lambda x, y: 1 <= x <= n and 1 <= y <= m
    
    drs, dcs = (1, 0, 0, -1), (0, -1, 1, 0)
    ds = ('d', 'l', 'r', 'u')

    route = []
    for i in range(k):
        for d, dr, dc in zip(ds, drs, dcs):
            nx, ny = x + dr, y + dc
            if in_range(nx, ny) and abs(nx - r) + abs(ny - c) <= k - i - 1:
                x, y = nx, ny
                route.append(d)
                break
                    
    answer = ''.join(route)
    return answer