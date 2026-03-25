def solve(board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r, c):
            if r < 0 or c < 0 or board[r][c] != 'O' or c == col or r == row:
                return
            board[r][c] = 'r'
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        row = board[0]
        col = board[0][0]

        for c in range(col):
            dfs(0, c)
            dfs(row - 1, c)

        for r in range(row):
            dfs(r, 0)
            dfs(r, col - 1)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'r':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'


