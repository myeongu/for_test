# https://www.acmicpc.net/problem/18352

from collections import deque


n, m, k, x = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)

result = []
visited = [False] * (n + 1)
visited[x] = True

q = deque([(x, 0)])
while q:
    now, cost = q.popleft()
    if cost == k:
        result.append(now)
    elif cost > k:
        break
    for i in edges[now]:
        if visited[i]:  # 방문한 적이 있는 경우
            continue
        visited[i] = True
        q.append((i, cost + 1))

result.sort()
if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)
