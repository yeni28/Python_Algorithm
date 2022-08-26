class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Node를 사용해서 트리 만들어보기

root = Node(1) #root 노드 만들기

# 2,3을 root의 왼쪽과 오른쪽에 추가

root.left = Node(2)
root.right = Node(3)

# 4,5를 2번의 왼쪽과 오른쪽에 추가

root.left.left = Node(4) #Node(2).left
root.left.right = Node(5) #Node(2).right

# 전위순회
# 방문처리는 노드에 데이터를 출력해주면 된다.
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

