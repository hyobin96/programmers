def solution(board, skill):
    row, col = len(board), len(board[0])
    prefix_board = [[0] * (col + 1) for _ in range(row + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        
        prefix_board[r1][c1] += degree
        prefix_board[r1][c2 + 1] -= degree
        prefix_board[r2 + 1][c1] -= degree
        prefix_board[r2 + 1][c2 + 1] += degree 
        
    for i in range(row):
        for j in range(1, col):
            prefix_board[i][j] += prefix_board[i][j - 1]
            
    for j in range(col):
        for i in range(1, row):
            prefix_board[i][j] += prefix_board[i - 1][j]
            

        
    count = 0
    for i in range(row):
        for j in range(col):
            board[i][j] += prefix_board[i][j]
            if board[i][j] > 0:
                count += 1
                
    # for r in board:
    #     print(r)
    
    answer = count
    return answer