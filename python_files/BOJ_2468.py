# DFS
'''
1. 높이를 1부터 올리면서 temp_graph에 높이 이하인 곳은 0으로 저장
2. dfs 돌리면서 labeling으로 count
3. count 저장하면서 print(max)
'''
import sys

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
sys.setrecursionlimit(10**6)

# LRUD
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 이 dfs의 핵심? 계속 labeling하는 것
# 실수한 point = dfs에 no need인 return을 넣은 것
def dfs(x, y, label, height):
    # 1. Visited
    visited[x][y] = label

    # 2. Next with label
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] > height:
                dfs(nx, ny, label, height)


find_max = []
for row in graph:
    find_max.append(max(row))
found_max = max(find_max)

all_heights_safe_region = []
# For looping all possible heights
for ht in range(found_max):
    g_label = 0
    visited = list(list(0 for _ in range(N)) for _ in range(N))
    # For looping all regions (Just for one height)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] > ht:
                g_label += 1
                dfs(i, j, g_label, ht)
    all_heights_safe_region.append(g_label)
print(max(all_heights_safe_region))