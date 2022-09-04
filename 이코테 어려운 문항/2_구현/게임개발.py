def turn_left(d):
    if d == 0:
        return 3
    return d - 1


direct_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

visited = [[False] * (m) for _ in range(n)]
visited[x][y] = True

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

result = 1
while True:
    print(x, y)
    # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우
    wrapped = True
    for i in range(4):
        dx, dy = direct_dict[i][0], direct_dict[i][1]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if data[nx][ny] == 0 and visited[nx][ny] == False:
            wrapped = False
    if wrapped:  # 둘러싸인 경우
        dx, dy = direct_dict[direction][0], direct_dict[direction][1]
        x, y = x - dx, y - dy  # 뒤로 한 칸 이동
        if data[x][y] == 1:  # 뒤쪽 방향이 바다인 경우
            break
        continue

    direction = turn_left(direction)
    dx, dy = direct_dict[direction]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

    if not visited[nx][ny] and data[nx][ny] == 0:
        x, y = nx, ny  # 이동
        visited[x][y] = True
        result += 1
        print("move!")
        continue

print(result)
