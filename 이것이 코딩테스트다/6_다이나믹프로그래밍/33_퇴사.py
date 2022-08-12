## https://www.acmicpc.net/problem/14501

# 마지막 날 N
n = int(input())

data = [[]]
for _ in range(n):
    data.append(list(map(int, input().split())))

days = [[(0,0)]] # 날짜 자체를 index로 사용하면 됨!
days.append([(data[1][1], data[1][0])]) # [(최대 금액, 끝나는 날)]

result = 0
for i in range(1, n+1):
    day_max = []
    end_date = i - 1 + data[i][0]
    if end_date > n:
        continue

    for day in days:
        for each in day:
            if i > each[1]: # 끝나는 날 이후인 경우
                cur_max = each[0] + data[i][1]
                result = max(result, cur_max)
                day_max.append((cur_max, end_date))
    days.append(day_max)

# print(days)
print(result)

## 예시 답안
'''
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
'''