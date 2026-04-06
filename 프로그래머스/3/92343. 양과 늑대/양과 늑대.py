def solution(info, edges):
    node_count = len(info)
    tree = [[] for _ in range(node_count)]
    for u, v in edges:
        tree[u].append(v)
    
    def dfs():
        max_sheep = 0
        stack = [(0, 0, 0, [0])] # curr, sheep, wolf, nxt_nodes
        while stack:
            curr, sheep, wolf, nxt_nodes = stack.pop()
            sheep, wolf = sheep + (info[curr] ^ 1), wolf + info[curr]
            # print(curr, sheep, wolf)
            if sheep <= wolf:
                continue
                
            max_sheep = max(max_sheep, sheep)
            nxt_nodes.remove(curr)
            nxt_nodes += tree[curr][:]
            for nxt in nxt_nodes:
                stack.append((nxt, sheep, wolf, nxt_nodes[:]))
        
        return max_sheep
        

    max_sheep = dfs()
    answer = max_sheep
    return answer