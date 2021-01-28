# 게임 개발

N, M = map(int, input().split())

x, y, direction = map(int, input().split())

array = []

for i in range(N):
    array.append(list(map(int, input().split())))

# 방문 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
#람다식 사용함!!!
d = [[0] * M for i in range(N)]

# 처음 위치 방문 처리
d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면에 가지 않은 칸이 존재하면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)