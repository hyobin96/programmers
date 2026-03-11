import sys
sys.setrecursionlimit(20000)

def solution(begin, target, words):
    def count_diff(word1, word2):
        count = 0
        for w1, w2 in zip(word1, word2):
            count += int(w1 != w2)
        return count
    
    s = set(words)
    s.add(begin)
    if target not in s:
        return 0
    s.add(target)
    n = len(s)
    word_idx_map = dict()
    idx_word_map = dict()
    for i, word in enumerate(s):
        word_idx_map[word] = i
        idx_word_map[i] = word
    
    begin_idx, target_idx = word_idx_map[begin], word_idx_map[target]
    visited = [0] * n
    is_one_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            is_one_diff[i][j] = int(1 == count_diff(idx_word_map[i], idx_word_map[j]))
            is_one_diff[j][i] = is_one_diff[i][j]
            
    def dfs(u, cnt):
        nonlocal min_cnt, visited
        if u == target_idx:
            min_cnt = min(min_cnt, cnt)
            return
        
        for i in range(n):
            if visited[i] or not is_one_diff[u][i]:
                continue
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0
            
    min_cnt = 2e9
    visited[begin_idx] = 1
    # print(begin_idx, target_idx, visited)
    dfs(begin_idx, 0)
            
    answer = min_cnt
    return answer