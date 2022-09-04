from collections import deque
from copy import deepcopy


n = int(input())

indgree = [0] * (n+1)
each_time = [0] * (n+1)
after_cls = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    each_time[i] = data[0]
    for d in data[1:-1]:
        indgree[i] += 1
        after_cls[d].append(i)


result = deepcopy(each_time)
q = deque()

for i in range(1, n+1):
    if indgree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in after_cls[now]:
        result[i] = max(result[i], result[now] + each_time[i])
        indgree[i] -= 1

        if indgree[i] == 0:
            q.append(i)

print(result)
