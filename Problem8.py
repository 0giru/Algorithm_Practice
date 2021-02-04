# 음료수 얼려 먹기

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 인접 좌표를 모두 방문하여 1로 만듦
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            # print([i, j])
            result += 1

print(result)