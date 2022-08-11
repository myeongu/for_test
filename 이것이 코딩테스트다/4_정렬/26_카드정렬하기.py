# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))


cal = 0

while len(cards) != 1:
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    sum_value = one + two
    cal += sum_value

    heapq.heappush(cards, sum_value)

print(cal)
