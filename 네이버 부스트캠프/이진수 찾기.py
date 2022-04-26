## 문제
# N(1 ≤ N ≤ 31)자리의 이진수가 있다. 
# 이러한 이진수 중에서, L(1 ≤ L ≤ N)개 이하의 비트만 1인 것을 크기 순으로 나열했을 때, 
# I번째로 나오는 이진수를 구해내는 프로그램을 작성하시오. 이진수는 0으로 시작할 수도 있다.

## 입력
# 첫째 줄에 세 정수 N, L, I가 주어진다. I번째 이진수가 있는 입력만 주어진다.

## 출력
# 첫째 줄에 답을 출력한다.

def Print_Answer(n_i, bit_i, find, cnt):
    if bit_i == 0:
        if cnt < n:
            print(0, end='')
            Print_Answer(n_i, bit_i, find, cnt+1)

    elif n_i == bit_i:
        if dp[n_i-1][bit_i-1] < find:
            find -= dp[n_i-1][bit_i-1]
            print(1, end='')
        else:
            print(0, end='')
        Print_Answer(n_i - 1, bit_i - 1, find, cnt+1)
    else:
        if dp[n_i-1][bit_i] < find:
            find -= dp[n_i-1][bit_i]
            print(1, end='')
            Print_Answer(n_i-1, bit_i-1, find, cnt+1)
        else:
            print(0, end='')
            Print_Answer(n_i-1, bit_i, find, cnt+1)


N, L, I = map(int, input().split())

dp = [[1 for _ in range(L+1)] for _ in range(N+1)]

# dp 구성
for n in range(1, N+1):
    for l in range(1, L+1):
        dp[n][l] = dp[n-1][l-1] + dp[n-1][l]

Print_Answer(N, L, I, 0)

# 1의 개수가 m 이하인 n자리 이진수의 개수
# = 1의 개수가 m-1 이하인 n-1자리 이진수 개수 + 1의 개수가 m 이하인 n-1자리 이진수 개수
# (점화식으로 세우면, dp[n][m] =  dp[n-1][m-1] + dp[n-1][m])