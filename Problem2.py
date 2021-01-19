#숫자 카드 게임

#N = 행의 개수, M = 열의 개수
N, M = map(int, input().split())

list_num = []
list_list = []

#각 행을 리스트화 해서 \리스트를 담는 리스트\에 넣는다
for i in range(N):
    list_list.append(list(map(int, input().split())))

#\리스트를 담은 리스트\에 담긴 리스트들의 최소값을 찾아주기 위해 sort() 사용
for i in range(N):
    list_list[i].sort()

#각 리스트들이 sort() 되었으므로 인덱스 0번째 원소가 최소값
#0번째 원소들을 선택하여 또다시 리스트에 넣는다
for i in range(N):
    list_num.append(list_list[i][0])

#이 중 최댓값을 찾기 위해 내림차순 정렬
list_num.reverse()

print(list_num[0])

#################################################################
#위 방법을 min() 함수를 이용해 다시 풀어보자

N, M = map(int, input().split())

temp_num = list()

for i in range(N):
    temp_list = list(map(int, input().split()))
    temp_min = min(temp_list)
    temp_num.append(temp_min)

print(max(temp_num))

#실행 결과 훨씬 간단한 코딩으로 같은 동작을 할 수 있다.