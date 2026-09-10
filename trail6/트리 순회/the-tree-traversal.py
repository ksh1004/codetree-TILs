n = int(input())

left = [0] * 26
right = [0] * 26

for _ in range(n):
    x, l, r = input().split()
    left[ord(x) - ord("A")] = l
    right[ord(x) - ord("A")] = r

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(left[ord(node) - ord("A")])
    preorder(right[ord(node) - ord("A")])

def inorder(node):
    if node == '.':
        return
    inorder(left[ord(node) - ord("A")])
    print(node, end='')
    inorder(right[ord(node) - ord("A")])

def postorder(node):
    if node == '.':
        return
    postorder(left[ord(node) - ord("A")])
    postorder(right[ord(node) - ord("A")])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()