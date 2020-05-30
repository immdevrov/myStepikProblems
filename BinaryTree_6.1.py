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

in_ = []
pre_ = []
post_ = []

def in_order(node: Node):
    if node.left != -1:
        in_order(tree[node.left])
    in_.append(str(node.key))
    if node.right != -1:
        in_order(tree[node.right])

def pre_order(node: Node):
    pre_.append(str(node.key))
    if node.left != -1:
        pre_order(tree[node.left])
    if node.right != -1:
        pre_order(tree[node.right])


def post_order(node: Node):
    if node.left != -1:
        post_order(tree[node.left])
    if node.right != -1:
        post_order(tree[node.right])
    post_.append(str(node.key))

in_order(tree[0])
print(' '.join(in_))
pre_order(tree[0])
print(' '.join(pre_))
post_order(tree[0])
print(' '.join(post_))
