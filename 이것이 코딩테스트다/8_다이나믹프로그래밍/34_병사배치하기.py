# https://www.acmicpc.net/problem/18353

n = int(input())

soldiers = list(map(int, input().split()))
soldiers = soldiers[::-1]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        cur = soldiers[i]
        if cur > soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
