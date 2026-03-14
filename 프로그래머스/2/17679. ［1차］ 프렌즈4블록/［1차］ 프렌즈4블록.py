def solution(m, n, board):
    
    def is_2_to_2(i, j):
        if not board[i][j]:
            return False
        if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
            return True
        return False
            
    def erase_block(ijs):
        nonlocal board
        for i, j in ijs:
            for r in range(i, i + 2):
                for c in range(j, j + 2):
                    board[r][c] = ''
                    
    def down():
        nonlocal board
        for i in range(m - 1, 0, -1):
            for j in range(n):
                if not board[i][j]:
                    for k in range(i - 1, -1, -1):
                        if board[k][j]:
                            board[i][j] = board[k][j]
                            board[k][j] = ''
                            break
                            
        
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        ijs = []
        for i in range(m - 1):
            for j in range(n - 1):
                if is_2_to_2(i, j):
                    ijs.append((i, j))
        if not ijs:
            break
        erase_block(ijs)
        down()
    
    total = 0
    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                total += 1
    
    answer = total
    return answer