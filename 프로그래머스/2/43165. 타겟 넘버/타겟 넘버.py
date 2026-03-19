def solution(numbers, target):
    def dfs(target):
        stack = [(numbers[0], 1), (-numbers[0], 1)] # 현재 값, 다음 타겟 인덱스
        count = 0
        while stack:
            u, t_idx = stack.pop()
            if t_idx == len(numbers):
                if u == target:
                    count += 1
                continue
            t_n = numbers[t_idx]
            stack.append((u + t_n, t_idx + 1))
            stack.append((u - t_n, t_idx + 1))
        
        return count
        
    return dfs(target)