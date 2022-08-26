class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node('+')

root.left = Node('*')
root.right = Node('E')

root.left.left = Node('*')
root.left.right = Node('D')

root.left.left.left = Node('/')
root.left.left.right = Node('C')

root.left.left.left.left = Node('A')
root.left.left.left.right = Node('B')

# 전위순회
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

print(preorder(root))

# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

print(inorder(root))


# 후위순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print(postorder(root))
