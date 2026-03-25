############################## Right side view ####################################
class Solution:
    def rightSideView(self, root):
        res = []

        def check(node, n):
            if not node:
                return

            if n == len(res):
                res.append(node.val)

            check(node.right, n + 1)
            check(node.left, n + 1)

        check(root, 0)
        return res


"""class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        visited = []
        queue = [root]
        while queue:
            n = len(queue)
            emp = []
            for i in range(n):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                emp.append(cur.val)
            visited.append(emp[-1])
        return visited"""

################################ left side view ############################################
"""class Solution:
    def leftSideView(self, root):
        if root is None:
            return []
        visited = []
        queue = [root]
        while queue:
            n = len(queue)
            emp = []
            for i in range(n):
                cur = queue.pop(0)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                emp.append(cur.val)
            visited.append(emp[0])
        return visited"""

class Solution:
    def leftSideView(self, root):
        res = []

        def check(node, n):
            if not node:
                return

            if n == len(res):
                res.append(node.val)

            check(node.left, n + 1)
            check(node.right, n + 1)


        check(root, 0)
        return res