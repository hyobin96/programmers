# 90도 4방향, 1방향마다 40 * 40, 좌 -> 우, 상 -> 하 이중 for문
# 매번 400번 비교
# 최종 횟수는 4 * 40 * 40 * 400 = 64 * 1e4
 
def solution(key, lock):
    def rotate_arr(arr):
        m = len(arr)
        nxt_arr = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                nxt_arr[j][m - i - 1] = arr[i][j]
        
        # for row in nxt_arr:
        #     print(row)
        return nxt_arr
    
    def validate_key(i, j, key, lock):
        n, m = len(lock), len(key)
        for r in range(n):
            for c in range(n):
                if i <= r < i + m and j <= c < j + m:
                    if key[r - i][c - j] ^ lock[r][c] == 0:
                        return False                        
                else:
                    if lock[r][c] == 0:
                        return False
        return True

    keys = [key]
    curr_arr = key
    for _ in range(4):
        nxt_arr = rotate_arr(curr_arr)
        keys.append(nxt_arr)
        curr_arr = nxt_arr
        
    n, m = len(lock), len(key)
        
    for i in range(-m, n, 1):
        for j in range(-m, n, 1):
            for k in keys:
                if validate_key(i, j, k, lock):
                    return True    
    
    return False