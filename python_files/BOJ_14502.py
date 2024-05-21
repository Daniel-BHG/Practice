from itertools import combinations
import sys
import copy

N, M = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))
sys.setrecursionlimit(10**8)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def virus_dfs(x, y):
    # 1. Visited
    visited[x][y] = 1

    # 2. Next
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if temp_graph[nx][ny] == 0 and temp_graph[nx][ny] != 1:
                temp_graph[nx][ny] = 2
                virus_dfs(nx, ny)


# 1. Wall setting by combinations
# 2. Virus DFS
# 3. Count safe region and appending
# 4. Print max

### 1. Wall setting
## Way 1
# possible_wall = []
# for x in range(N):
#     for y in range(M):
#         if graph[x][y] == 0:
#             possible_wall.append((x, y))

## Way 2
# Appending all zeros' position (x,y) to list
possible_wall = list((x, y) for x in range(N) for y in range(M) if graph[x][y] == 0)

combination_wall = combinations(possible_wall, 3) # Check all combinations of walls
final_wall = []
for com in combination_wall: # record all combinations
    final_wall.append(com)

result = []
for pos_set in final_wall: # pos_set ((0 0) (0 1) (1 1))
    temp_graph = copy.deepcopy(graph) # initialize with deepcopy
    visited = list(list(0 for _ in range(M)) for _ in range(N))
    for pos in pos_set: # pos (0 0)
        temp_graph[pos[0]][pos[1]] = 1 # set three walls to temp_graph
    
    ### 2. Virus DFS : Virus infection
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2 and visited[i][j] == 0:
                virus_dfs(i, j)
    
    ### 3. Count safe region
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                cnt += 1
    result.append(cnt)

print(max(result))