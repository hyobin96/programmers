# 대칭 이용

def solution(m, n, startX, startY, balls):
    def get_dist_square(x, y, b):
        return (x - b[0]) ** 2 + (y - b[1]) ** 2
    
    def is_45(b):
        x, y = b
        return startX == startY and x == y
    
    def is_135(b):
        x, y = b
        return startX == n - startY and x == n - y
    
    answer = []
    
    up = [(startX, startY + (n - startY) * 2)]
    down = [(startX, -startY)]
    left = [(-startX, startY)]
    right = [(startX + 2 * (m - startX), startY)]
    corner_45_up = [(startX + 2 * (m - startX), startY + (n - startY) * 2)]
    corner_45_down = [(-startX, -startY)]
    corner_135_up = [(-startX, startY + (n - startY) * 2)]
    corner_135_down = [(startX + 2 * (m - startX), -startY)]
    
    for b in balls:
        dist_min = 2e9
        if startX == b[0]:
            directions = left + right
            if startY > b[1]:
                directions += up
            else:
                directions += down
            for x, y in directions:
                dist_min = min(dist_min, get_dist_square(x, y, b))
        elif startY == b[1]:
            directions = up + down
            if startX < b[0]:
                directions += left
            else:
                directions += right
            for x, y in directions:
                dist_min = min(dist_min, get_dist_square(x, y, b))
            
        elif is_45(b):
            directions = up + down + left + right
            if startX < b[0]:
                directions += corner_45_down
            else:
                directions += corner_45_up
            for x, y in directions:
                dist_min = min(dist_min, get_dist_square(x, y, b))
        elif is_135(b):
            directions = up + down + left + right
            if startX < b[0]:
                directions += corner_135_up
            else:
                directions += corner_135_down
            for x, y in directions:
                dist_min = min(dist_min, get_dist_square(x, y, b))
        else:
            for x, y in up + down + left + right:        
                dist_min = min(dist_min, get_dist_square(x, y, b))    
        answer.append(dist_min)
        
    return answer