## 입력 조건
# 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다. (1≤N≤1,OOO,1≤M≤10)
# 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다. (1≤K≤M)

## 출력조건 
# 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 줄력합니다.

def get_combination(a):
    return a*(a-1)/2

n, m = map(int, input().split())
weights_list = list(map(int, input().split()))
weights_dict = {}
for weight in weights_list:
    try:
        weights_dict[weight] += 1
    except:
        weights_dict[weight] = 1

result = get_combination(n)
for count in weights_dict.values():
    if count > 1:
        result -= get_combination(count)

print(int(result))

## 예시 답안
'''   
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)'''