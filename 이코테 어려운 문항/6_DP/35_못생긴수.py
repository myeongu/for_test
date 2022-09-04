n = int(input())

agly = [1] * (n)

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    agly[i] = min(next2, next3, next5)

    if agly[i] == next2:
        i2 += 1
        next2 = agly[i2] * 2
    if agly[i] == next3:
        i3 += 1
        next3 = agly[i3] * 3
    if agly[i] == next5:
        i5 += 1
        next5 = agly[i5] * 5
    print(agly)

print(agly[-1])
