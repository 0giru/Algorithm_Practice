# 이진 탐색 소스코드 구현(재귀 함수)

# 탐색할 배열, 시점, 종점, 찾을 값이 필요
def binary_search(par_list, par_target, par_start, par_end):
    if par_start > par_end:
        return None
    
    mid = (par_start + par_end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if par_list[mid] == par_target:
        return mid
    # 타겟이 중간점보다 앞에 있는 경우
    elif par_list[mid] > par_target:
        return binary_search(par_list, par_target, par_start, mid-1)
    # 타겟이 중간점보다 뒤에 있는 경우
    elif par_list[mid] < par_target:
        return binary_search(par_list, par_target, mid+1, par_end)

# 원소의 개수와 타겟 입력받기
n, target = map(int, input().split())

# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("no result")
else:
    print(result+1)
