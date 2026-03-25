grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands(grid):
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        def find(i,j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            find(i,j+1)
            find(i,j-1)
            find(i+1,j)
            find(i-1,j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    find(i,j)
                    cnt += 1
        return cnt
print(numIslands(grid))