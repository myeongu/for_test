# 나의 답안(이진 탐색)
n = int(input())
n_list = input().split()
m = int(input())
m_list = input().split()

n_list.sort()


def binary_search(target, start, end):
    mid = (start + end) // 2
    if n_list[mid] == target:
        return True
    while start < end:
        if n_list[mid] > target:
            return binary_search(target, start, mid - 1)
        else:
            return binary_search(target, mid + 1, end)
    return False


for i in m_list:
    if binary_search(i, 0, n-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

# 예시 답안1 (계수 정렬)
'''
# N(가게의 부품 수) 입력받기
n = int(input())
array = [0] * 1000000

# 가게에 있는 전체 부품 번호 입력 받은뒤 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호 공백으로 구분하여 입력
x = list(map(int, input().split()))
# 손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''

# 예시 답안2(set() 함수)
'''
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes',  end=' ')
    else:
        print('no', end=' ')
'''
