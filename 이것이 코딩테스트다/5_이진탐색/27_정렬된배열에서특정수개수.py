'''
n, x = map(int, input().split())
array = list(map(int, input().split()))


def do_binary(l, target, start, end):
    mid = (start + end) // 2

    if start > end:
        return True

    if target == array[mid]:
        l.append(mid)
        do_binary(l, x, start, mid - 1)
        do_binary(l, x, mid + 1, end)
        # return None
    else:
        if array[mid] > target:
            end = mid - 1
            do_binary(l, x, start, end)
            # return None
        else:
            start = mid + 1
            do_binary(l, x, start, end)
            # return None
    print(l)
    return None


def count_x(x):
    if x not in array:
        return -1
    answer_list = []
    start = 0
    end = len(array) - 1
    do_binary(answer_list, x, start, end)

    return len(answer_list)


print(count_x(x))
'''

# 모범 답안
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
