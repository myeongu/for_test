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