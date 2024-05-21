n = 8
graph = [[0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
     	 [1, 0, 0, 1, 1, 0, 0, 0],
     	 [0, 1, 1, 0, 0, 1, 0, 0],
     	 [0, 0, 1, 0, 0, 0, 1, 1],
     	 [0, 0, 0, 1, 0, 0, 0, 0],
     	 [0, 0, 0, 0, 1, 0, 0, 1],
     	 [0, 0, 0, 0, 1, 0, 1, 0]]

###########
### DFS ###
###########

# Check for visited node
visited_dfs = [0 for _ in range(n)]

# dfs(0, n)

###########
### BFS ###
###########

from collections import deque

visited_bfs = [0 for _ in range(len(graph[0]))]

def bfs(s):
    # 1. Start node
    dq = deque()
    dq.append(s)

    # 2. Looping
    while dq:
        # Next visit node 체크
        next = dq.popleft()
        if visited_bfs[next] == 0: # 중복 방문 제거
            visited_bfs[next] = 1
            print(chr(next + ord('A')), end=' ')
            for i in range(len(graph[0])): # 방문한 node의 friends appending
                if graph[next][i] == 1 and visited_bfs[i] == 0:
                    dq.append(i)
bfs(0)