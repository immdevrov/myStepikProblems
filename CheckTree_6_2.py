n = int(input())


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


tree = []

for i in range(n):
    key, left, right = [int(i) for i in input().split(' ')]
    tree.append(Node(key, left, right))

def wrong_tree(node: Node):
    if node.left != -1:
        if node.key < tree[node.left].key:
            raise Exception("wrong")
        wrong_tree(tree[node.left])
    if node.right != -1:
        if node.key > tree[node.right].key:
           raise Exception("wrong")
        wrong_tree(tree[node.right])


if n == 0:
    print('CORRECT')
else:
    try:
        wrong_tree(tree[0])
        print('CORRECT')
    except:
        print('INCORRECT')
