import sys

sys.setrecursionlimit(4000000)

def solution(nodes, edges):
    arr = [[] for _ in range(1000001)]
    
    for u, v in edges:
        arr[u].append(v)
        arr[v].append(u)
        
        
    visited = [0] * (1000001)
    visited_key = 1
    
    forest = []
        
    def dfs(u):
        nonlocal visited, forest
        visited[u] = visited_key
        
        forest[-1].append(u)
        
        for v in arr[u]:
            if visited[v] == visited_key:
                continue
                
            dfs(v)
        
        
    for n in nodes:
        if visited[n]:
            continue
            
        forest.append([])
        dfs(n)
        
    # 부모일 때와 자식일 때 홀짝인지 역홀짝인지 판단
    tree_p = [[] for _ in range(len(forest))]
    tree_c = [[] for _ in range(len(forest))]
    for i, tree in enumerate(forest):
        for node in tree:
            tree_p[i].append(0 if len(arr[node]) % 2 == node % 2 else 1)
            tree_c[i].append(0 if (len(arr[node]) - 1) % 2 == node % 2 else 1)
            
    # print(tree_p)
    # print(tree_c)
    
    answer = [0, 0]
    
    for i in range(len(forest)):
        t_p, t_c = tree_p[i], tree_c[i]
        if len(t_p) == 1:
            answer[t_p[0]] += 1
            continue
        s = sum(t_c)
        if s == 1:
            if len(t_c) == 2:
                answer[1] += 1
            answer[0] += 1
        elif s == len(t_c) - 1:
            answer[1] += 1
        # elif s == len(t_c) or s == 0:
            
            
        
    # print(forest)
        
    return answer