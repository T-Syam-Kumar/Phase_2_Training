from other_sums.binary_tree import root


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



    def inorderTraversal(self,root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.data)
            self.inorderTraversal(root.right)
        pass

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left.left = Node(10)
root.right.left.right = Node(11)
root.right.right.left = Node(12)
root.right.right.right = Node(13)
root.right.right.left.left = Node(14)
root.right.right.left.right = Node(15)
root.right.right.left.left = Node(16)
root.right.right.left.right = Node(17)
root.right.right.left.right = Node(18)
root.right.right.left.left = Node(19)
root.right.right.left.right = Node(20)
root.right.right.left.right = Node(21)
root.right.right.left.right = Node(22)
root.right.right.left.right = Node(23)
root.right.right.left.right = Node(24)
root.right.right.left.left = Node(25)




"""    def insertLeft(self, node):
        if self.left is None:
            self.left = node
            
    def insertRight(self, node):
        if self.right is None:
            self.right = node
            
    def removeLeft(self):
        if self.left is None:"""
