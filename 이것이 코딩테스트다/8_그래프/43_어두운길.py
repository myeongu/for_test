def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

edges = []
for i in range(m):
    # each way
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

parent = [i for i in range(n)]
total_save = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        total_save += cost
print(total_save)
