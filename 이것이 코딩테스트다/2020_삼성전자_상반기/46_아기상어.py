# https://www.acmicpc.net/problem/16236

from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():  # 모든 위치까지의 '최단 거리만' 계산
    dist = [[-1] * n for _ in range(n)]  # 값이 -1인 경우 도달할 수 없음을 의미

    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 상어가 지나갈 수 있는 조건
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist  # 모든 위치까지의 최단 거리 리스트


def find(dist):  # 최단 거리 리스트를 기반으로, 물고기를 찾음
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # (도달 가능) and (먹을 수 있는 물고기)
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist:  # 가장 가까운 물고기
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:  # 먹을 수 있는 물고기 없는 경우
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0  # 현재 먹은 물고기 수

while True:
    value = find(bfs())  # 먹을 수 있는 물고기 위치

    if value == None:  # 먹을 수 있는 물고기가 없는 경우
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]  # 현재 위치 변경
        result += value[2]  # 이동 거리 추가

        array[now_x][now_y] = 0  # 먹은 위치는 0으로 치환
        ate += 1

        if ate >= now_size:  # 크기 증가
            now_size += 1
            ate = 0


""" # 틀린 풀이 -> 세부 조건 불만족
from collections import deque


n = int(input())  # 공간의 크기 nxn
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    if 9 in data:
        col = data.index(9)
        shark_pos = [i, col]
        graph[i][col] = 0

shark_size = 2
shark_eat = 0  # 현재까지 먹은 물고기 수
result = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


while True:  # 각 루프가 물고기를 찾는 과정
    visited = [[False] * n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = True  # 출발 노드
    # graph[shark_pos[0]][shark_pos[1]] = 0  # 기존 상어 위치

    q = deque([shark_pos + [0]])  # (x, y, 이동 시간)
    count = 0

    flag = True
    while flag:
        if len(q) == 0:
            break

        x, y, c = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue

            if graph[nx][ny] == 0:
                q.append(([nx, ny] + [c+1]))
                visited[nx][ny] = True
            elif graph[nx][ny] <= 6:
                if shark_size > graph[nx][ny]:
                    shark_pos = [nx, ny]
                    graph[nx][ny] = 0
                    count = c + 1
                    shark_eat += 1
                    q.append(shark_pos + [c+1])
                    if shark_eat == shark_size:
                        shark_size += 1
                        shark_eat = 0
                    flag = False
                    break

                elif shark_size == graph[nx][ny]:
                    q.append(([nx, ny] + [c+1]))
                    visited[nx][ny] = True
    result += count
    if len(q) == 0:
        break

print(result)
"""
