import heapq

t = int(input())
INF = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

test_case = []
for _ in range(t):
    n = int(input())

    case = []
    for _ in range(n):
        row = list(map(int, input().split()))
        case.append(row)

    test_case.append(case)

for case in test_case:  # 테스트 케이스 수만큼 반복
    n = len(case)

    # 최단 거리 테이블
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    # 시작노드 큐 삽입
    q = [(case[x][y], x, y)]
    distance[x][y] = case[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:  # 방문한 적이 있는 경우
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 맵 벗어나는 경우
                continue
            cost = dist + case[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
