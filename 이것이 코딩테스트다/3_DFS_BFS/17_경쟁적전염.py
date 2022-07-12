# https://www.acmicpc.net/problem/18405

from collections import deque
import pprint

n, k = map(int, input().split())
grid = [] # 1행은 index 0
for _ in range(n):
    grid.append(list(map(int, input().split())))
s, fx, fy = map(int, input().split())

dx = [-1, 0, 1, 0] # 북, 시계방향
dy = [0, 1, 0, -1]

# 바이러스 초기 위치 저장
virus = dict()
for i in range(n):
    for j in range(n):
        v_num = grid[i][j]
        if v_num == 0:
            continue
        if v_num in virus.keys():
            virus[v_num].append((i,j))
        else:
            virus[v_num] = [(i,j)]

# 초기 바이러스 queue 삽입 - virus 숫자 순
q = deque()
for v_position in sorted(virus.keys()):
    for p in virus[v_position]:
        q.append(p)

second = 0
while second < s: # s초 동안 수행
    for _ in range(len(q)): # 현재 q 길이 만큼 수행하면 1초
        x, y = q.popleft()
        v_num = grid[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] != 0:
                continue
            grid[nx][ny] = v_num
            q.append((nx, ny))
    second += 1
    if q == None:
        break
    # print(second, '초: ', q)
    # pprint.pprint(grid)

print(grid[fx-1][fy-1])

# 모범 답안
'''
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
 
target_s, target_x, target_y = map(int, input().split())
 
# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
'''