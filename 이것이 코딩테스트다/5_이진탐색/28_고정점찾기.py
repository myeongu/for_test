def binary_search(array, start, end):
    mid = (start + end) // 2
    if start > end:
        return False

    if array[mid] == mid:
        return mid

    if array[mid] > mid:
        return binary_search(array, start, mid - 1)
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)


n = int(input())
array = list(map(int, input().split()))

start = 0
end = n - 1
binary_result = binary_search(array, start, end)
if binary_result:
    print(binary_result)
else:
    print(-1)
