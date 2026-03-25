class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count1 = self.maxDepth(root.left)
        count2 = self.maxDepth(root.right)
        return max(count1,count2)+1