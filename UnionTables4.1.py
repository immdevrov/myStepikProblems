# n, m = 5, 5
# r = [1, 1, 1, 1, 1, 1]
# commands = [
#     [3, 5],
#     [2, 4],
#     [1, 4],
#     [5, 4],
#     [5, 3]
# ]

n, m = map(int, input().split(' '))
r = [int(i) for i in input().split(' ')]
commands = []
for i in range(m):
    commands.append(map(int, input().split(' ')))

parent = [i for i in range(n)]

def find(i):
    while i != parent[i]:
        parent[i] = find(parent[i])
        i = parent[i]
    return parent[i]

max_ = max(r)

for destination, source in commands:
    destination_id = find(destination - 1)
    source_id = find(source - 1)
    if not source_id == destination_id:
        parent[source_id] = destination_id
        r[destination_id] += r[source_id]
        if r[destination_id] > max_:
            max_ = r[destination_id]
        r[source_id] = 0
    print(max_)
