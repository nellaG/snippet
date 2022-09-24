""" https://leetcode.com/problems/path-sum-ii/ """


from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        self.dfs(root, targetSum, [], output)
        return output

    def dfs(self, root, targetsum, ls, res):
        if root:
            # subtract each val from root to leaf
            is_leaf = not root.left and not root.right
            if is_leaf and targetsum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, targetsum - root.val, ls + [root.val], res)
            self.dfs(root.right, targetsum - root.val, ls + [root.val], res)
