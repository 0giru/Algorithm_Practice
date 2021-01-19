# p.92 큰 수의 법칙

result = 0

# 공백으로 구분하여 받는 입력 map 함수 사용에 주의
N, M, K = map(int, input().split())

list1 = []

list1 = list(map(int, input().split()))

#오름차순 배열
list1.sort()
num_pres = list1[len(list1)-1]
num_vice = list1[len(list1)-2]

#첫번째 방법
while True:
    if M == 0:
        break
    else:
        for i in range(K):
            result = result + num_pres
            M -= 1
            if M == 0:
                break

        if(M != 0):
            result += num_vice
            M -= 1

print(result)

#####################################################
#두번째 방법
Q = M // (K+1)
S = M % (K+1)

result = Q * num_pres * K
result += Q * num_vice
result += S * num_pres

print(result)