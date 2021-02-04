from collections import deque

N, M = map(int, input().split())

graph = []

# 상하좌우 이동을 고려할 땐 dx, dy를 사용하는 것도 고려해보자
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        


