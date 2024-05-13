# DFS
# nx, ny Direction
# 단지수 + 단지에 속하는 집의 수 출력 >> line별로 graph.count()

N = int(input())
graph = list(list(map(int, input())) for _ in range(N))
visited = list(list(0 for _ in range(N)) for _ in range(N))

# LRUD
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, label):
    # 1. Visited
    visited[x][y] = label

    # 2. Next
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, label)

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            dfs(i, j, cnt)

# Print
print(cnt) # 총 단지수
num_house = [0 for _ in range(cnt)]
for line in visited:
    for i in range(cnt):
        num_house[i] += line.count(i+1)
num_house.sort()
for j in range(len(num_house)):
    print(num_house[j])
