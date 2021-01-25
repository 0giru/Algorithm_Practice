# 상하좌우

N = int(input())

x, y = 1, 1

#operation will be R L U D
operation = input().split()

while True:
    if not operation:
        break
    else:
        temp = operation.pop(0)

        if temp == 'R':
            if y < N:
                y += 1
            elif y >= N:
                pass
        
        elif temp == 'L':
            if y > 1:
                y -= 1
            elif y < 1:
                pass
        
        elif temp == 'D':
            if x < N:
                x += 1
            elif x >= N:
                pass
        
        elif temp == 'U':
            if x > 1:
                x -= 1
            elif x <= 1:
                pass

print(x, y)
