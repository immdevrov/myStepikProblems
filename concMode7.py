import heapq

n, m = map(int, input().split(' '))
time = list(map(int, input().split(' ')))
l = [[0, i] for i in range(n)]

for f in time:
    t, p = heapq.heappop(l)
    print(p, t)
    t = t + f
    heapq.heappush(l, [t, p])
