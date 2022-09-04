# https://www.acmicpc.net/problem/10825

n = int(input())

data = []
for _ in range(n):
    d = input().split()
    data.append([d[0]] + list(map(int, d[1:])))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for d in data:
    print(d[0])
