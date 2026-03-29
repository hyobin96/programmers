import math
def solution(n, w, num):
    row, col = math.ceil(n / w), w
    grid = [[0] * col for _ in range(row)]
    # for r in grid:
    #     print(r)
    
    number = 1
    r, c, d = row - 1, 0, 1
    while number <= n:
        grid[r][c] = number
        
        if number % w == 0:
            r -= 1
            d *= -1
            number += 1
            continue
            
        number += 1
        c += d
        
    answer = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == num:
                count = 1
                for k in range(i - 1, -1, -1):
                    if grid[k][j]:
                        count += 1
                        continue
                    break
                answer = count
                break

    return answer