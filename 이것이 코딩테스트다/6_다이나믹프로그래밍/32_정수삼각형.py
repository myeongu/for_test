## https://www.acmicpc.net/problem/1932

# N: 삼각형의 크기
n = int(input())

tri = []
for _ in range(n):
    row = list(map(int, input().split()))
    tri.append(row)

# 합을 나타내는 삼각형
new_tri = []
new_tri.append([tri[0][0]]) # 초기화

for m in range(1, n):
    temp = [] # 합산 저장하는 row
    for i in range(m+1):
        if i == 0: # 각 행의 첫번째 숫자
            before = new_tri[m-1][0]
        elif i == m: # 각 행의 마지막 숫자
            before = new_tri[m-1][-1]
        else:
            before = max(new_tri[m-1][i-1], new_tri[m-1][i])
        temp.append(before + tri[m][i])
    new_tri.append(temp)

print(max(new_tri[-1]))

## 예시 답안
'''n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))'''