import sys
sys.setrecursionlimit(10**6)

def search(graph, x, y, N, color):
    if color == 'RG':
        if graph[x][y] == 'R' or graph[x][y] == 'G':
            graph[x][y] = -1
    else:
        if graph[x][y] == color:
            graph[x][y] = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if color == 'RG':   
                if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    search(graph, nx, ny, N, color)
            else:
                if graph[nx][ny] == color:
                    search(graph, nx, ny, N, color)


N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    graph.append(list(sys.stdin.readline()))

graph_copy = []

for i in range(0, len(graph)):
    graph_copy.append(graph[i].copy())

## 적녹 색약이 아닌사람일 때
group = [0] * 2

for i in range(N):
    for j in range(N):
        if graph[i][j] != -1:
            if graph[i][j] == 'R':
                group[0] += 1
                search(graph, i, j, N, 'R')
            elif graph[i][j] == 'G':
                group[0] += 1
                search(graph, i, j, N, 'G')
            elif graph[i][j] == 'B':
                group[0] += 1
                search(graph, i, j, N, 'B')

## 적녹 색약인 사람일 때
graph = graph_copy

for i in range(N):
    for j in range(N):
        if graph[i][j] != -1:
            if graph[i][j] == 'R' or graph[i][j] == 'G':
                group[1] += 1
                search(graph, i, j, N, 'RG')
            elif graph[i][j] == 'B':
                group[1] += 1
                search(graph, i, j, N, 'B')

for i in range(0, len(group)):
    print(group[i], end=" ")