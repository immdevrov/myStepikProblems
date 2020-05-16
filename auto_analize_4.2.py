# n, e, d = 6, 5, 3
# equals = [
#     [2, 3],
#     [1, 5],
#     [2, 5],
#     [3, 4],
#     [4, 2]
# ]
# non_equals = [
#     [6, 1],
#     [4, 6],
#     [4, 5]
# ]

n, e, d = map(int, input().split(' '))

equals = []
for i in range(e):
    equals.append(list(map(int, input().split(' '))))
non_equals = []
for i in range(d):
    non_equals.append(list(map(int, input().split(' '))))

parent = [i for i in range(n)]

def analize():
    for i, j in equals:
        j -= 1
        i -= 1
        parent[j] = parent[i]
    for i1, j1 in non_equals:
        i1 -= 1
        j1 -= 1
        if parent[i1] == parent[j1]:
            return 0
    return 1

print(analize())
