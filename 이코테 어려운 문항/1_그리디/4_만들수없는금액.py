n = int(input())

coin = list(map(int, input().split()))
coin.sort()

cur_max = 1

for c in coin:
    if c > cur_max:
        break
    cur_max += c

print(cur_max)
