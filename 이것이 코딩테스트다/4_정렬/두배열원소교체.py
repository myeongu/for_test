n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)
result = sum(array_a)
for i in range(k):
    if array_a[i] < array_b[i]:
        result += array_b[i] - array_a[i]
    else:
        break
print(result)

# 예시 답안
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] <b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
'''
