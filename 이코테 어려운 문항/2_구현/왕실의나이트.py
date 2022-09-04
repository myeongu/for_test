def get_col(c):
    if c == 'a':
        return 1
    elif c == 'b':
        return 2
    elif c == 'c':
        return 3
    elif c == 'd':
        return 4
    elif c == 'e':
        return 5
    elif c == 'f':
        return 6
    elif c == 'g':
        return 7
    elif c == 'h':
        return 8


pos = input()
row, col = int(pos[1]), get_col(pos[0])

dx = [2, -2, 2, -2, 1, -1, 1, -1]
dy = [1, 1, -1, -1, 2, -2, -2, 2]

count = 0
for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)
