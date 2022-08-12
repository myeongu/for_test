# 못생긴 수 = 2, 3, 5만을 소인수로 가지는 수
# 1도 못생긴 수로 가정
# n번째 못생긴 수를 찾는 프로그램

'''
n = int(input())

agly = [1]

while len(agly) < 2*n:
    two = [i * 2 for i in agly]
    three = [i * 3 for i in agly]
    five = [i * 5 for i in agly]

    agly += two + three + five

    agly = list(set(agly))
    print(agly)
agly.sort()

print(agly[n-1])
'''

# 모범 답안
n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    # print(next2, next3, next5)

print(ugly[n-1])
