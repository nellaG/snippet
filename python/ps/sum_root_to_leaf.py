""" https://leetcode.com/problems/sum-root-to-leaf-numbers/ """


class Solution:
    def sumNumbers(self, root) -> int:
        total = 0
        total = self.dfs(root, "")
        return total

    def dfs(self, root, num: str):
        if not root:
            return 0

        is_leaf = not root.left and not root.right
        num += str(root.val)
        if is_leaf:

            return int(num)
        return self.dfs(root.left, num) + self.dfs(root.right, num)
