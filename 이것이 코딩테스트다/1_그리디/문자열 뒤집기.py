## 입력 조건
# 첫째 줄에 O과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100민보다 직습니다

## 출력 조건
# 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력합니다.
s = input()

to_one = 0
to_zero = 0

if s[0] == '1':
    to_zero += 1
else:
    to_one += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            to_zero += 1
        else:
            to_one += 1

print(min(to_one, to_zero))