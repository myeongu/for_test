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

parent = [i for i in range(n+1)]
for _ in range(m):
    i, a, b = map(int, input().split())
    if i == 0:  # union
        union_parent(parent, a, b)
    elif i == 1:  # get
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")
