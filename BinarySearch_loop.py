def binary_search(par_list, par_target, par_start, par_end):
    while par_start <= par_end:
        mid = (par_start + par_end)//2

        if par_list[mid] == par_target:
            # 값을 찾는다면 mid 인덱스를 반환
            return mid
        # target이 list의 중앙 값보다 뒤에 있는 경우
        elif par_target > par_list[mid]:
            par_start = mid + 1
        # target이 list의 중앙 값보다 앞에 있는 경우
        elif par_target < par_list[mid]:
            par_end = mid - 1
    # return mid를 하지 못하고 while loop가 끝나면 None 반환
    return None

# 원소의 개수와 타겟 입력받기
n, target = map(int, input().split())

# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("값이 존재하지 않음")
else:
    print(result+1)