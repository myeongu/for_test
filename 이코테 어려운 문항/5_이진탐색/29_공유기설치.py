# https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())

home = []
for i in range(n):
    home.append(int(input()))
home.sort()

start = 1
end = home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = home[0]  # 첫번째 집에는 무조건 설치
    count = 1

    for i in range(n):
        if home[i] >= value + mid:
            value = home[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
