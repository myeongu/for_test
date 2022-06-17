## page 375

# test case
t = int(input())
case = []
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    each_case = []
    for i in range(n):
        each_case.append(data[m*i : m*i+m])
    case.append((n, m, each_case))


def result(each):
    n, m, data = each
    temp = []
    for i in range(n):
        temp.append(data[i][0])
    
    for j in range(1, m):
        new_temp = []
        for i in range(n):
            if i == 0:
                new = max(temp[i], temp[i+1]) + data[i][j]
            elif i == n-1 :
                new = max(temp[i-1], temp[i]) + data[i][j]
            else:
                new = max(temp[i-1], temp[i], temp[i+1]) + data[i][j]
            new_temp.append(new)
        
        temp = new_temp
    
    return max(temp)
            

# 각 케이스에 대해 결과 출력
for each in case:
    print(result(each))
    
## 예시 답안
'''
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
'''