# https://www.acmicpc.net/problem/18310

n = int(input())
data = list(map(int, input().split()))
data.sort()

index = n//2 - 1 if n % 2 == 0 else n // 2
print(data[index])
