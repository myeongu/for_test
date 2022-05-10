## 입력 조건
# 첫째 줄에 모험가의 수 N이 주어집니다. (1≤N≤100,OOO) .
# 둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

## 출력 조건 
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

n = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()

group = 0
count = 0
for fear in fear_list:
    count += 1
    if count >= fear:
        group += 1
        count = 0
    
print(group)