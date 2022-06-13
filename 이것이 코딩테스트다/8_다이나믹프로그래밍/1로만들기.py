## page 217
## 입력 조건

## 출력 조건

## 답안 예시

# 정수 X 입력
x = int(input())

# DP 테이블 초기화
d = [0] * 30001

# DP (바텀업)
for i in range(2, x+1):
    # 현재의 수에서 1을 뺀느 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])