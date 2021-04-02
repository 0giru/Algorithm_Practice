# 무한대 값 설정
INF = int(1e9)

# 노드와 간선의 개수 입력받기 노드 n 간선 m
n = int(input())
m = int(input())

# 2차원 리스트 생성 후 INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 본인으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보를 입력받아 그래프에 표시
for _ in range(m):
    a, b, c = map(int, input().split()) # a노드에서 b노드로 가는 비용이 c
    graph[a][b] = c

# 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph)