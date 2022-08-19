import heapq


n, m = map(int, input().split())

high_score = [[] for _ in range(n+1)]
low_score = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    high_score[a].append(b)
    low_score[b].append(a)

count = 0
for i in range(1, n+1):
    # 큰 값
    high = high_score[i][:]
    h = high_score[i][:]
    while h:
        now = heapq.heappop(h)
        further_high = high_score[now]
        for h_i in further_high:
            if h_i not in high:
                heapq.heappush(h, h_i)
                high.append(h_i)

    # 작은 값
    low = low_score[i][:]
    l = low_score[i][:]
    while l:
        now = heapq.heappop(l)
        further_low = low_score[now]
        for l_i in further_low:
            if l_i not in low:
                heapq.heappush(l, l_i)
                low.append(l_i)

    if len(high) + len(low) == n - 1:
        count += 1

print(count)

# 모범 답안
'''
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # A에서 B로 가는 비용을 1로 설정

# 경로가 존재 = a, b 사이의 비교 가능
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n+1):
    count = 0
    # i에 대해서 모든 경로가 존재하다면(비교 가능하다면), 순위 결정 가능
    for j in range(1, n+1): 
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
        if count == n:
            result += 1

print(result)
'''
