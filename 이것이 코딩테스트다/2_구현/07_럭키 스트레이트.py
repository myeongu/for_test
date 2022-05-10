## 입력 조건
# 첫째 줄에 점수 N이 정수로 주어집니다.(10≤N≤99,999.999) 단, 점수 N의 자릿수는 힝싱 짝수 형태로만 주어집니다. 
# 예를들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않습니다.

## 출력 조건
# 첫째 줄에 럭키스트레이트를 사용할 수 있다면 “LUCKY"를 사용할 수 없다면 "READY"를 줄력합니다.

score = input()
length = len(score) // 2
left, right = score[:length], score[length:]

left_score, right_score = 0, 0
for i in range(length):
    left_score += int(left[i])
    right_score += int(right[i])

if left_score == right_score:
    print("LUCKY")
else:
    print("READY")
