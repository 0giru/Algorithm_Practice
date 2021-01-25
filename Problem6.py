# a1
cur_pos = input()

cur_row = ord(cur_pos[0])
cur_col = int(cur_pos[1])

next_pos = []

count = 0

steps = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

for step in steps:
    next_pos.append(cur_col + step[0])
    next_pos.append(cur_row + step[1])
    if((next_pos[1] >= 97 and next_pos[1] <= 104) and (next_pos[0] >= 1 and next_pos[0] <= 8)):
        count += 1
        next_pos.pop()
        next_pos.pop()
    else:
        next_pos.pop()
        next_pos.pop()
        continue

print(count)