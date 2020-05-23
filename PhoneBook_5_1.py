
n = int(input())

table = ['not found' for i in range(1, 10000001)]
result = []
for i in range(n):
    command = [s for s in input().split(' ')]
    if command[0] == 'add':
        table[int(command[1])] = command[2]
    if command[0] == 'del':
        table[int(command[1])] = 'not found'
    if command[0] == 'find':
        result.append(table[int(command[1])])


for r in result:
    print(r)
