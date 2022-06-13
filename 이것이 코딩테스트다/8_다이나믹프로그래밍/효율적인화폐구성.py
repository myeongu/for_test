## page 226
## 입력 조건

## 출력 조건

## 답안 예시

# 정수 N, M 입력
n, m = map(int, input().split())
# N개의 화폐 단위 정보
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m+1)

# DP (바텀업)
d[0] = 0
for i in range(n): # n개의 화폐 단위
    for j in range(array[i], m+1): # 각 화폐 단위 이상의 값에 대해서
        d[j] = min(d[j], d[j - array[i]] + 1)

# 결과 출력
if d[m] == 10001: # M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
