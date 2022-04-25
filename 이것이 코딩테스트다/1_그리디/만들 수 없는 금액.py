## 입력 조건 
# 첫째 줄에는 동전의 개수틀 나타내는 양의 정수 N이 주어집니다. (1≤N≤1,OOO)
# 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다. 
# 이 때, 각 화폐 단위는 1,OOO,OOO 이하의 자연수입니다.

## 출력 조건 
# 첫째 즐에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.

n = int(input())
coin_list = list(map(int, input().split()))
coin_dict = {}

for coin in coin_list:
    try:
        coin_dict[coin] += 1
    except:
        coin_dict[coin] = 1

print(coin_dict)