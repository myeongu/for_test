# https://www.acmicpc.net/problem/11404


n = int(input())  # 도시 수
m = int(input())  # 버스 수

INF = int(1e9)
dist = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # 출발, 도착, 비용
    if c < dist[a][b]:
        dist[a][b] = c


# 대각 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


for i in range(1, n+1):
    s = ' '.join(list(map(str, dist[i]))[1:])
    s.replace('1000000000', '0')
    print(s)
