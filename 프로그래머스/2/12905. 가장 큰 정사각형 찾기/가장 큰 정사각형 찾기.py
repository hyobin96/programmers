# 0 1 1 1   0 1 1 1
# 1 1 1 1   1 0 2 2
# 1 1 1 1   1 2 2 2
# 0 0 1 0   0 0 0 0


# 0 1 1 1
# 1 0 2 2
# 1 2 2 3 
# 0 0 0 0

def solution(board):
    n, m = len(board), len(board[0])
    
    max_area = max(board[0])
    
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
            max_area = max(max_area, board[i][j])
            
    answer = max_area ** 2
    return answer