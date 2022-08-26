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


g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
count = 0
for i in range(p):
    g_i = int(input())
    p_g_i = find_parent(parent, g_i)

    if p_g_i == 0:
        break

    union_parent(parent, g_i, p_g_i-1)
    count += 1
    print(parent)


print(count)
