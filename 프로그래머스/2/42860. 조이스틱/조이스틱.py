def solution(names):
    def dfs(name, total, idx):
        nonlocal min_count
        
        a = name[idx]
        if a != 'A':
            up, down = ord('Z') - ord(a) + 1, ord(a) - ord('A')
            total += min(up, down)
            name[idx] = 'A'
            
        dist1, dist2 = 0, 0
        next_idx1 = idx
        next_idx2 = idx
        for i in range(1, n):
            right_idx = (idx + i) % n
            if name[right_idx] != 'A':
                dist1 = i
                next_idx1 = right_idx
                break
                
        for i in range(1, n):
            left_idx = (idx - i + n) % n
            if name[left_idx] != 'A':
                dist2 = i
                next_idx2 = left_idx
                break

                
        if not dist1 and not dist2:
            min_count = min(min_count, total)
            return   
        
        if dist1:
            dfs(name[::], total + dist1, next_idx1)
            
        if dist2:
            dfs(name[::], total + dist2, next_idx2)
            
     
    min_count = 2e8
    n = len(names)

    dfs(list(names), 0, 0)
    
    answer = min_count
    return answer