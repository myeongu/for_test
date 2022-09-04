def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


n = int(input())
store = list(map(int, input().split()))
store.sort()

m = int(input())
customer = list(map(int, input().split()))

for c in customer:
    if binary_search(store, c, 0, n-1):
        print("yes")
    else:
        print("no")
