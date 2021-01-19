#1이 될 때 까지

N, K = map(int, input().split())
count = 0

while True:
    if N == 1:
        break
    else:
        if(N%K == 0):
            N = N//K
            count += 1
        else:
            N -= 1
            count += 1

print(count)