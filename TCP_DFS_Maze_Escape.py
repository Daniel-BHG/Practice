"""
5 6
101010
111111
000001
111111
111111
"""

from collections import deque
import time

N, M = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(N))
start = time.time()

# LRUD
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        if x == N-1 and y == M-1: # If last node
            return graph[N-1][M-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    dq.append((nx, ny))
    # return graph[N-1][M-1]


print(bfs(0, 0))
end = time.time()
print(f"{end - start:.5f}s")
