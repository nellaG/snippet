""" https://leetcode.com/problems/path-sum/ """

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        is_leaf = not root.left and not root.right
        if is_leaf and root.val == targetSum:
            return True
        resum = targetSum - root.val
        return self.hasPathSum(root.left, resum) or self.hasPathSum(root.right, resum)
