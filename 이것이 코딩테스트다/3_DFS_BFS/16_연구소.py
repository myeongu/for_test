## https://www.acmicpc.net/problem/14502

# N, M
n, m = map(int, input().split())
data = [] # 초기 상태
current = [[0] * (m) for _ in range(n)] # 현재 상태

for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)

# 뱡향 설정 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최종 결과 값 (max)
result = 0

# 현재 위치에서 바이러스 전체로 퍼지도록 (DFS)
def spread(x, y):
    for i in range(4): # 4가지 방향에 대해
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if current[nx][ny] == 0:
            current[nx][ny] = 2
            spread(nx, ny)

# 퍼진 뒤 안전 영역 넓이 구하기
def safe(current):
    area = 0
    for i in range(n):
        for j in range(m):
            if current[i][j] == 0:
                area += 1
    return area

# 벽 3개를 세우는 모든 경우에 대해서 최대 면적 (DFS & 재귀)
def dfs(count):
    global result

    if count == 3: # 벽 3개를 다 세운 경우
        for i in range(n):
            for j in range(m):
                current[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if current[i][j] == 2:
                    spread(i, j)
        result = max(result, safe(current))
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

## 예시 답안
'''n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)'''