# 특정 원소가 속한 집합을 찾기(루트 찾기-루트가 같으면 같은 집합에 속하는 것이므로)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

"""
경로 압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
"""

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    A = find_parent(parent, a)
    B = find_parent(parent, b)
    # A가 B보다 작다면 a가 b의 부모가 된다
    if A < B:
        parent[B] = A
    # B가 A보다 작다면 b가 a의 부모가 된다
    else:
        parent[A] = B

# 노드와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end='')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')