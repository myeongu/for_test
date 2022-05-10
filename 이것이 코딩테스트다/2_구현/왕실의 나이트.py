## 입력 조건
# 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
# 입력 문자는 a1처럼 열과 행으로 이뤄진다.

## 출력 조건
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

## 내 풀이
# pos = input()
# col, row = pos[0], int(pos[1])
# print(col, row)

# full_col = ['c','d','e','f']
# full_row = [3,4,5,6]

# if col in full_col and row in full_row:
#     answer = 8
# elif col in ['a', 'h'] and row in [1, 8]:
#     answer = 2
# elif col in ['a', 'h']:
#     if row in full_row:
#         answer = 4
#     else: # 2, 7
#         answer = 3
# elif row in [1, 8]:
#     if col in full_col:
#         answer = 4
#     else:
#         answer = 3
# elif col in ['b', 'g']:
#     if row in [2, 7]:
#         answer = 4
#     elif row in full_row:
#         answer = 6
# elif row in [2,7]:
#     if col in ['b', 'g']:
#         answer = 4
#     elif col in full_col:
#         answer = 6

# print(answer)

## 예시 답안
# 현재 위치
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)