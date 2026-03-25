class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        visited = []
        r = 0
        while queue:
            arr = []
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                arr.append(cur.val)
            if r%2 == 0:
                visited.append(arr)
            else:
                visited.append(arr[::-1])
            r += 1
        return visited