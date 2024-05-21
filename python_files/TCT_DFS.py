"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""

x_row, y_col = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(x_row))

visited = [[0 for _ in range(y_col)] for _ in range(x_row)]

# 좌우상하
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]

def dfs(x, y, label):
    # 1. Visited
    visited[x][y] = label

    # 2. Next LRUD
    for i in range(4):
        nrow = ncol = 0
        nrow = x + row[i]
        ncol = y + col[i]
        if 0 <= nrow < x_row and 0 <= ncol < y_col:
            if graph[nrow][ncol] == 0 and visited[nrow][ncol] == 0:
                dfs(nrow, ncol, label)

def ndfs(x, y, label):
    while

cnt = 0
for i in range(x_row):
    for j in range(y_col):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)


print(cnt)