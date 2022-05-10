## 입력 조건
# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (N≥3,M≤50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# 방향 d의 값은 다음과 같다.
    # - O : 북쪽 
    # -	1 : 동쪽
    # -	2 : 님쪽
    # -	3 : 서쪽
# 셋째 줄부터 맵이 육지인지	바다인지 입력한다. 
# N개의 줄에 맵의 상태가 북쪽부터 남쪽	순서대로 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 
# 맵의 외괵은 힝상 바다로 되어 있다.
# -O:육지 -1:바다
# 처음에 게임 캐릭터가 위치한 칸의 상태는 힝상 육지이다.

## 출력 조건
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

## 얘시 답안
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 초기화 된 맵
d = [[0] * m for _ in range(n)]

# 현재 위치, 방향
x, y, direction = map(int, input().split())
d[x][y] = 1 

# 전체 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시물레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
# 정답 출력
print(count)