# https://www.acmicpc.net/problem/18428

from itertools import combinations


def is_hide(block):
    global array, teacher

    dx = [0, 1, 0, -1]  # row
    dy = [1, 0, -1, 0]  # col

    for x, y in teacher:
        for i in range(4):  # 4가지 방향
            flag = True
            nx, ny = x, y
            # print(nx, ny)
            while flag:
                nx = nx + dx[i]
                ny = ny + dy[i]
                if nx >= n or nx < 0 or ny >= n or ny < 0:
                    break
                if (nx, ny) in block:
                    break
                if array[nx][ny] == "S":
                    return False
    return True


n = int(input())
array = []
empty = []
teacher = []
for i in range(n):
    row = input().split()
    for j, each in enumerate(row):
        if each == "X":
            empty.append((i, j))
        elif each == "T":
            teacher.append((i, j))
    array.append(row)

blocks = combinations(empty, 3)
for block in blocks:
    if is_hide(block):
        print("YES")
        break
else:
    print("NO")
