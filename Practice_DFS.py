# DFS 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
    # 0번 노드와는 아무것도 연결되어 있지 않음
    [], 
    # 1번 노드와 2번, 3번, 8번 노드가 연결되어있음
    [2, 3, 8],
    # 2번 노드와 1번, 7번 노드가 연결되어있음
    [1, 7],
    # 3번 노드와 1번, 4번, 5번 노드가 연결되어있음
    [1, 4, 5],
    # 4번 노드와 3번, 5번 노드가 연결되어있음
    [3, 5],
    # 5번 노드와 3번, 4번 노드가 연결되어있음
    [3, 4],
    # 6번노드와 7번노가 연결되어있음
    [7],
    # 7번 노드와 2번, 6번, 8번 노드가 연결되어있음
    [2, 6, 8],
    # 8번 노드와 1번, 7번 노드가 연결되어있음
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
# 처음에는 모두 방문되어 있지 않으므로 모두 FALSE
# 노드는 0부터 취급하여 총 9개의 노드
visited = [False] * 9

# 정의된 DFS 함수 호출
# 1번 노드 부터 방문 시작
dfs(graph, 1, visited)
