# page 152
## 입력 조건

## 출력 조건

## 답안 예시

from collections import deque

# N, M 입력
n, m = map(int, input().split())
# 2차원 리스트 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 (상 항 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드
def bfs(x, y):
    # Queue 구현을 위한 deque
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치 기준 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문 시에만 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

# BFS 수행 결과
print(bfs(0, 0))