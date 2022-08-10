# https://www.acmicpc.net/problem/10825

n = int(input())
data = []
for _ in range(n):
    name, ko, en, ma = input().split()
    each = (name, int(ko), int(en), int(ma))
    data.append(each)

sorted_data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for d in sorted_data:
    print(d[0])

# 모범 답안
'''n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])'''
