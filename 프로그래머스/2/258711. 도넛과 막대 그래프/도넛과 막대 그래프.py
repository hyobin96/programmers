# 들어오는 간선이 없는데 나가는 간선이 2개 이상이라면 생성한 정점
# 생성한 정점에서 나가는 간선은 무시해야 함
# 각 그래프 판별 필요
# 막대 모양 그래프의 마지막 점은 자기한테 들어오는 간선이 단 하나거나 없고 나가는 간선이 없을 때
# 8자 모양 그래프의 중심점은 나한테 2개 들어오고 2개 나가는 점
# 도넛 모양 그래프의 중심점은 나한테 1개 들어오고 1개 나가는 점
# 각 점에 간선리스트 만들기
# 들어오는 간선, 나가는 간선 따로 저장

import sys

sys.setrecursionlimit(1000000)

def solution(edges):
    def add_dict(d, a, b):
        if a in d:
            d[a].add(b)
        else:
            d[a] = set()
            d[a].add(b)
        
    def dfs(u, graph):
        nonlocal vertexs
        cnt = 1
        if u in vertexs:
            vertexs.remove(u)
        if u in graph:
            for v in graph[u]:
                if v in vertexs:
                    cnt += dfs(v, graph)
        return cnt
            
    out_edge_d = dict()
    in_edge_d = dict()
    vertexs = set()
    for a, b in edges:
        vertexs.add(a)
        vertexs.add(b)
        add_dict(out_edge_d, a, b)
        add_dict(in_edge_d, b, a)
    
    added_vertex = 0
    total = 0
    for vertex in vertexs:
        if vertex not in in_edge_d and vertex in out_edge_d and len(out_edge_d[vertex]) >= 2:
            added_vertex = vertex
            total = len(out_edge_d[vertex])
            for v in out_edge_d[vertex]:
                in_edge_d[v].remove(vertex)
            del out_edge_d[vertex]
            break
    vertexs.remove(added_vertex)
            
    # print(out_edge_d)
    # print(in_edge_d)
    막대_끝점들, 도넛_중심점들, 팔자_중심점들 = [], [], []
    for vertex in vertexs:
        # print(vertex)
        if (vertex not in in_edge_d or len(in_edge_d[vertex]) in (0, 1)) and vertex not in out_edge_d:
            막대_끝점들.append(vertex)
        elif vertex in in_edge_d and len(in_edge_d[vertex]) == 2 and vertex in out_edge_d and len(out_edge_d[vertex]) == 2:
            팔자_중심점들.append(vertex)
            
    
    answer = [added_vertex, total - len(막대_끝점들) - len(팔자_중심점들), len(막대_끝점들), len(팔자_중심점들)]
    return answer