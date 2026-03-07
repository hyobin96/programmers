def solution(tickets):
    airport_mapper = dict()
    s = set()
    for start, target in tickets:
        s.add(start)
        s.add(target)
    
    airports = sorted(list(s))
    # print(airports)
    
    idx_mapper = dict()
    for i, airport in enumerate(airports):
        airport_mapper[airport] = i
        idx_mapper[i] = airport
        
    # print(airport_mapper)
    n = len(airport_mapper)
    
    for i in range(len(tickets)):
        tickets[i][0], tickets[i][1] = airport_mapper[tickets[i][0]], airport_mapper[tickets[i][1]]
    tickets.sort()
    # print(tickets)
    
    edges = [[] for _ in range(n)]
    for u, v in tickets:
        edges[u].append(v)
        
    # print(edges)
    
    visited = [[[0] * n for _ in range(n)] for _ in range(n)]
    route = []
    routes = []
    def dfs(u):
        nonlocal visited
        if len(route) == len(tickets) + 1:
            routes.append(route[::])
        
        for i, v in enumerate(edges[u]):
            if visited[u][v][i]:
                continue
            visited[u][v][i] = 1
            route.append(v)
            dfs(v)
            visited[u][v][i] = 0
            route.pop()
            
    icn_idx = airport_mapper["ICN"]
    route.append(icn_idx)
    dfs(icn_idx)
    # print(routes)
    routes.sort()
    # print(routes)
    answer = [idx_mapper[i] for i in routes[0]]
    return answer