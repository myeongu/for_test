import heapq


n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n+1)]  # 노드 연결 정보, 비용(시간) 저장
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
dist = [INF] * (n+1)


def cal_cost(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        time, now = heapq.heappop(q)
        if dist[now] < time:
            continue

        for i in graph[now]:
            cost = time + i[1]  # 현재 노드와 연결된 다른 노드
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


cal_cost(c)

count = 0
max_time = 0
for d in dist:
    if d != INF:
        count += 1
        max_time = max(max_time, d)

print(count-1, max_time)  # 시작 노드는 제외
