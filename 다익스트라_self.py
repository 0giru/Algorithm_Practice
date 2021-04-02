INF = 999999999

# 전체 노드와 간선 개수 입력
node, weight = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 방문 리스트 초기화
# 구현의 편의를 위해 1번 인덱스부터 노드번호와 맞추어 사용
visited = [False for _ in range(node+1)]

# 최단 거리 테이블
distance = [INF for _ in range(node+1)]

graph = [[] for _ in range(node+1)]

# 노드_간선 정보 입력
# i노드로부터 e노드까지 w만큼의 가중치가 존재
for _ in range(weight):
    i, e, w = map(int, input().split())
    graph[i].append((w, e))

# 최단거리 리스트 인덱스 반환
def get_least_value():
    min_value = INF
    index = 0
    for i in range(1, node+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[0] = True
    visited[start] = True
    distance[start] = 0
    for nodes in graph[start]:
        distance[nodes[1]] = nodes[0]
    
    for _ in range(node-1):
        index = get_least_value()
        visited[index] = True
        for nodes in graph[index]:
            cost = distance[index] + nodes[0]
            if cost < distance[nodes[1]]:
                distance[nodes[1]] = cost
            else:
                continue

dijkstra(start)

print(distance)