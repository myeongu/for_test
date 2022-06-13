## page 223
## 입력 조건

## 출력 조건

## 답안 예시

# N 입력
n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# DP (바텀업)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

# 결과 출력
print(d[n])
