def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())

parent = [i for i in range(n+1)]  # 초기 부모는 자기 자신
# edge = []
for i in range(n):
    row = input().split()
    for j in range(i, n):
        if row[j] == "1":
            # edge.append((i+1, j+1))  # 주어진 배열 기준 edge 추출
            union_parent(parent, i+1, j+1)

way = map(int, input().split())


print(parent)
# print(edge)
result_set = set()
for i, w in enumerate(way):
    result_set.add(find_parent(parent, w))
    if len(result_set) >= 2:
        print("NO")
        break
    if len(result_set) == 1 and i == m-1:
        print("YES")
