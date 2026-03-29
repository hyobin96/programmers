# node - abc 방문배열
# infection 관리

def solution(n, infection, edges, k):
    def permu(arr, k):
        nonlocal tree, infection, max_count
        if len(arr) == k:
            # print(arr)
            max_count = max(max_count, count_infections(arr, tree, infection))
            return
        
        for i in range(1, 4):
            if arr and arr[-1] == i:
                continue
            arr.append(i)
            permu(arr, k)
            arr.pop()
            
    def init(edes, n, infection):
        tree = [[[] for _ in range(4)] for _ in range(n + 1)]
        for u, v, pipe in edges:
            tree[u][pipe].append(v)
            tree[v][pipe].append(u)
        
        return tree
    
    def count_infections(perm_arr, tree, begin_node):
        # print(perm_arr)
        infections = set()
        infections.add(begin_node)
        
        for pipe in perm_arr:
            for infection in list(infections):
                visited = [0] * (len(tree) + 1)
                stack = [infection]
                while stack:
                    node = stack.pop()
                    for next_node in tree[node][pipe]:
                        if visited[next_node] or next_node in infections:
                            continue
                        visited[next_node] = 1
                        infections.add(next_node)
                        stack.append(next_node)
                
        # print(infections)
        return len(infections)
                    
    tree = init(edges, n, infection)
    max_count = 1
    permu([], k)
    
    answer = max_count
    return answer