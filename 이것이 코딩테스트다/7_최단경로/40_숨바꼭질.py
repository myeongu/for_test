import heapq

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n+1)

# 출발점: 1번 노드
q = [(0, 1)]
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:  # 이미 방문한 적이 있는 경우
        continue

    for i in graph[now]:  # 현재 노드와 연결된 노드들
        cost = 1 + dist
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

max_dist = max(distance[1:])
count = 0
index = INF
for i, d in enumerate(distance):
    if d == max_dist:
        count += 1
        index = min(index, i)
print(index, max_dist, count)

# 모범 답안
'''
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heqppush(q, (cost, i[0]))


start = 1
dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
'''
