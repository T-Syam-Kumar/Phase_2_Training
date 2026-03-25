class Solution:
    def min(self, root):
        while root.left:
            root = root.left
        return root.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None and root.right is None: # No Children
                return None
            if root.left is None: return root.right # 1 children - only right node
            if root.right is None: return root.left # 1 children - only left node
            # if 2 children we can work with 2 cases to replace
            # 1. Max in left side(most right node)
            # 2. Min in right side(most left node)
            # we will work with 2nd case
            min_val = self.min(root.right)
            root.val = min_val
            root.right = self.deleteNode(root.right,min_val)
        return root
