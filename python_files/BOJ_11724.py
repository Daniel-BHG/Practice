node, edge = map(int, input().split())
list_edge = list(list(map(int, input().split())) for _ in range(edge))
graph = list(list(0 for _ in range(node)) for _ in range(node))
visited = list(0 for _ in range(node))

# Making graph
for elem in list_edge:
    # edge
    graph[elem[0] - 1][elem[1] - 1] = 1
    graph[elem[1] - 1][elem[0] - 1] = 1

def dfs(v, label):
    # 1. Visited
    visited[v] = label

    # 2. Next node
    for i in range(node):
        if not visited[i] and graph[v][i] == 1:
            dfs(i, label)

cnt = 0
for i in range(node):
    if not visited[i]:
        cnt += 1
        dfs(i, cnt)
print(cnt)