# https://www.acmicpc.net/problem/18310

n = int(input())
home = list(map(int, input().split()))
home.sort()

average = sum(home) / len(home)
min_dif = 1e9
if len(home) == 1:
    print(home[0])

# for i, h in enumerate(home):
#     dif = abs(average - h)
#     if dif >= min_dif:
#         print(home[i-1])
#         break
#     # if dif > min_dif:
#     #     print(home[i-1])
#     min_dif = min(min_dif, dif)
# # print(min_dif)
