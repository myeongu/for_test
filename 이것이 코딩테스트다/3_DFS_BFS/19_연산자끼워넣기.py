# https://www.acmicpc.net/problem/14888

'''from itertools import permutations


n = int(input()) # 수의 개수
n_list = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

def do_plus(a, b):
    return a + b

def do_minus(a, b):
    return a - b

def do_multiple(a,b):
    return a * b

def do_divide(a,b):
    if a < 0:
        return -((-a)//b)
    return a // b

def do_cal(cal_num, a, b):
    if cal_num == 0:
        return do_plus(a, b)
    elif cal_num == 1:
        return do_minus(a, b)
    elif cal_num == 2:
        return do_multiple(a, b)
    else:
        return do_divide(a, b)

# 연산 순서에 대해 모든 케이스 구하기
permute_list = []
permute_list += [0] * plus
permute_list += [1] * minus
permute_list += [2] * multiple
permute_list += [3] * divide

permute_set = set(list(permutations(permute_list)))

max_result = -1e9
min_result = 1e9
for cal_list in list(permutations(permute_list)):
    result = n_list[0]
    for i in range(1, n):
        result = do_cal(cal_list[i-1], result, n_list[i])
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)'''

# 모범 답안

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)