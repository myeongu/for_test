## 입력 조건
# 첫째 줄에 하나의 문자열 S가 주어집니다.(1≤S의길이≤10,OOO)

## 출력 조건
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

string = input()
num_type = [str(i) for i in range(10)]

num = 0
result = ''
for s in string:
    if s in num_type:
        num += int(s)
    else:
        result += s
result = ''.join(sorted(result))
if num != 0:
    result += str(num)
print(result)

## 예시 답안
'''data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))'''