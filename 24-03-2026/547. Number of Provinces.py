arr = [1,2,4,5,3,6]
ans = []
pr = 1
for i in range(len(arr)):
    pr = pr*arr[i]
"""for i in range(len(arr)):
    val = pr / arr[i]
    ans.append(val)


def solve(board):
    row = len(board)
    col = len(board[0])


    def dfs(i,j):
        if board[i][j] != "O":
            return
        board[i][j] = "K"
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)

    for i in [0,len(board)-1]:
        for j in [0,len(board[0])-1]:
            if board[i][j] == "O":
                dfs(i,j)
    for x in range(row):
        for y in range(col):
            if board[x][y] == "K":
                board[x][y] = "O"
            elif board[x][y] == "O":
                board[x][y] = "X"
    print(board)
"""

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


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]