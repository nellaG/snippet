""" https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        hmap = []

        return self.dfs(root, k, hmap)

    def dfs(self, root, k, hmap):
        if root:
            subt = k - root.val
            if subt in hmap:
                return True
            else:
                if root.val not in hmap:
                    hmap.append(root.val)
            return self.dfs(root.left, k, hmap) or self.dfs(root.right, k, hmap)
        return False
