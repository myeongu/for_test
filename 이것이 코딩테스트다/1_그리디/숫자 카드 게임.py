## 입력 조건
# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주 어진다(1≤N,M≤100)
# 둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 1O,OOO이하의 자연수이다.

## 출력 조건
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

n, m = map(int, input().split())

result = 0
for _ in range(n):
    row = map(int, input().split())
    
    min_in_row = min(row)
    result = max(result, min_in_row)

print(result)