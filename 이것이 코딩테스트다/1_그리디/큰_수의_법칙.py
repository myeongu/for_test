## 입력 조건 (N: 배열의 크기, M: 숫자가 더해지는 횟수, K)
# 첫째줄에 N(2≤N≤1,OOO), M(1≤M≤10,OOO), K(1≤K≤10,OOO)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 1 O.OOO 이하의 수로 주어진다.
# 입력으로 주어지는 K는 힝상 M보다 작거나 같다.

## 출력 조건
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 딥을 출력한다.

## 면구의 풀이
n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()
max_n = n_list[-1]
second_n = n_list[-2]

result = 0
max_flag = True
while m // k >= 1:
    if max_flag:
        result += max_n * k
        m = m - k
    else:
        result += second_n
        m = m - 1
    max_flag = not max_flag

if max_flag:
    result += max_n * m
else:
    result += second_n
    result += max_n * (m-1)

print(result)


## 제시된 정답 (단순한 방식)
'''
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수 
second = data[n - 2] # 두 번쌔로 큰 수

result = 0
while True: 
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출 
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m== 0: # m이 0이라면 반복문 탈출 
        break
    result += second # 두 번쌔로 큰 수를 한 번 더하기 
    m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력
'''

## 제시된 정답2 (효율적 방식: k개의 first, 1개의 second가 반복되는 수열로 생각)
'''
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수 
second = data[n - 2] # 두 번쌔로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번쌔로 큰 수 더하기
print(result) # 최종 답안 출력
'''