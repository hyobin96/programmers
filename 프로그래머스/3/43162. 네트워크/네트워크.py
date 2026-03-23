def solution(n, computers):
    def dfs(u, visited):
        # print("u: ", u)
        visited[u] = 1
        stack = [u]
        while stack:
            u = stack.pop()
            # print(computers[u])
            for i, v in enumerate(computers[u]):
                if visited[i] or v == 0:
                    continue
                visited[i] = 1
                stack.append(i)
    
    visited, cnt = [0] * n, 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i, visited)
        cnt += 1
        
    answer = cnt
    return answer