# https://www.acmicpc.net/problem/3190
## 입력 조건
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

## 출력 조건
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

'''import pprint
from collections import deque

def change_direction_to_L(dir):
    if dir == [0, 1]:
        return [-1, 0]
    elif dir == [1, 0]:
        return [0, 1]
    elif dir == [0, -1]:
        return [1, 0]
    elif dir == [-1, 0]:
        return [0, -1]

def change_direction_to_D(dir):
    if dir == [0, 1]:
        return [1, 0]
    elif dir == [1, 0]:
        return [0, -1]
    elif dir == [0, -1]:
        return [-1, 0]
    elif dir == [-1, 0]:
        return [0, 1]

N = int(input())
K = int(input())
apple_list = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col = map(int, input().split())
    apple_list[row-1][col-1] = 1 # 사과 위치 1로 표현
L = int(input())
second_list = []
direction_list = []
for _ in range(L):
    sec, dir = input().split()
    second_list.append(int(sec)) # 초를 담는 리스트
    direction_list.append(dir) # 방향을 담는 리스트(L, D)

before_mat = apple_list.copy() # 초기 matix
before_mat[0][0] = -1 # 뱀의 위치는 -1로 표현
second = 0
flag = True
direction = [0, 1] # 초기는 오른쪽 방향
sneak = deque([ [0,0] ])

while flag:
    second += 1
    head = sneak[0]    

    new_head = head[0] + direction[0], head[1] + direction[1] 
    if (new_head[0] in [-1, N]) or (new_head[1] in [-1, N]): # 벽을 벗어나는 경우
        flag = False
        break
    
    new_mat = before_mat.copy()
    if before_mat[new_head[0]][new_head[1]] == 1: # 사과를 만났을 때
        sneak.appendleft(new_head)
        new_mat[new_head[0]][new_head[1]] = -1
        before_mat = new_mat.copy()
    elif before_mat[new_head[0]][new_head[1]] == -1: # 이전 matrix에서 몸통 부분에 부딪혔을 때
        flag = False
        break
    else:
        sneak.appendleft(new_head)
        tail = sneak.pop()
        new_mat[new_head[0]][new_head[1]] = -1
        new_mat[tail[0]][tail[1]] = 0
        before_mat = new_mat.copy()
    
    if second in second_list:
        index = second_list.index(second)
        if direction_list[index] == 'L':
            direction = change_direction_to_L(direction)
        elif direction_list[index] == 'D':
            direction = change_direction_to_D(direction)
    # pprint.pprint(new_mat)
    
print(second)'''

## 답안 예시
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
