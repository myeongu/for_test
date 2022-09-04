n, m = map(int, input().split())

INF = int(1e9)
company = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            company[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    company[a][b] = 1
    company[b][a] = 1

x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            company[b][c] = min(company[b][c], company[b][a] + company[a][c])

print(company[1][k] + company[k][x])
