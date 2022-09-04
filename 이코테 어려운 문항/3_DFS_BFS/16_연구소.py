# https://www.acmicpc.net/problem/14502

from collections import deque
from copy import deepcopy
from itertools import combinations


def bfs(arr, v):
    q = deque(v)
    count = len(v)  # 초기 바이러스 수
    while q:  # 바이러스가 다 퍼저나갈 때까지
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append((nx, ny))
                    count += 1
    # print(count)
    return count


n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

array = []
empty = []
virus = []
for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    for j, d in enumerate(data):
        if d == 0:
            empty.append((i, j))
        elif d == 2:
            virus.append((i, j))
wall_num = n * m - len(virus) - len(empty)

result = 0
for data in list(combinations(empty, 3)):
    new_array = deepcopy(array)
    for d in data:
        new_array[d[0]][d[1]] = 1
    cur_count = n * m - wall_num - 3 - bfs(new_array, virus)
    result = max(result, cur_count)

print(result)
