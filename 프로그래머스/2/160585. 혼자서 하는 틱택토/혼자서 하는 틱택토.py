# 완탐

def solution(board):
        
    def is_same(game):
        for i in range(3):
            if board[i] != game[i]:
                return False
        return True
    
    def is_end(prev, game):
        ans = prev * 3
        garo = False
        sero = False
        daegak = False
        
        for i in range(3):
            if game[i] == ans:
                return True
            if game[0][i] + game[1][i] + game[2][i] == ans:
                return True
        
        if game[0][0] + game[1][1] + game[2][2] == ans:
            return True
        if game[2][0] + game[1][1] + game[0][2] == ans:
            return True
            
        return False

    def dfs(prev, game):
        nonlocal answer, visited
        
        if is_same(game):
            answer = 1
            return
        
        if is_end(prev, game):
            return

        for i in range(3):
            for j in range(3):
                if visited[i][j]:
                    continue
                visited[i][j] = 1
                curr = 'O'
                if prev == 'O':
                    curr = 'X'
                temp = game[i][::]
                game[i] = game[i][:j] + curr + game[i][j+1:]
                dfs(curr, game)
                game[i] = temp
                visited[i][j] = 0
    
    game = ['...'] * 3
    visited = [[0] * 3 for _ in range(3)]
    answer = 0
    dfs('X', game)
            
    return answer