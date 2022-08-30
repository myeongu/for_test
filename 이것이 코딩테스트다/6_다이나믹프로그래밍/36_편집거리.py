# 문자열 A, B
# A -> B로 편집
# 1) 삽입, 2) 삭제, 3) 교체

# 두 문자가 같은 경우: dp[i][j] = dp[i-1][j-1]
# 두 문자가 다른 경우(삽입, 삭제, 교체): dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

def get_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 2차원 dp 테이블
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]


str1 = input()
str2 = input()

print(get_dist(str1, str2))
