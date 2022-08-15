
n, m = map(int, input().split())
array = list(map(int, input().split()))


def cal_rest(x):  # x는 mid
    result = 0
    for t in array:
        if t > x:
            result += t-x
        else:
            continue
    return result


def binary_search(target, start, end):  # 길이 기준
    mid = (start + end) // 2
    if cal_rest(mid) == target:
        return mid
    while start < end:
        if cal_rest(mid) > target:
            return binary_search(target, mid+1, end)
        else:
            return binary_search(target, start, mid-1)
    if cal_rest(mid) > target:
        return mid
    else:
        return mid - 1


print(binary_search(6, 1, max(array)))

# 예시 답안
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에 result 기록
        start = mid + 1

print(result)
'''
