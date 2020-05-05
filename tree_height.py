import sys
sys.setrecursionlimit(20000)

n = int(input())
parents = input().split(' ')
tree = [[] for i in range(n)]
for i in range(n):
    elem = int(parents[i])
    if elem != -1:
        tree[elem].append(i)
    else:
        root = i

def height(r):
    h = 1
    for v in tree[r]:
        h = max(h, 1+height(v))
    return h

print(height(root))
