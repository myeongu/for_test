## 입력 조건
# 첫째 줄에 N(2≤N≤100,OOO)과 K(2≤K≤100,OOO)가 공백으로 구분되며 각각 자연수로 주어진다.
# 이 때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

## 출력 조건
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

n, k = map(int, input().split())

count = 0
while n != 1:
    if n % k == 0:
        n = n//k
    else:
        n -= 1
    count += 1

print(count)

## 답안 예시
'''n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    
    result += 1
    n //= k

result += (n-1)
print(result)'''