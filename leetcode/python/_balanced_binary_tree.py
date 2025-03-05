# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    is_balanced: bool = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traverseTree(root)

        return self.is_balanced

    def traverseTree(self, root: Optional[TreeNode]) -> int:
        if not root or not self.is_balanced:
            return 0

        left = self.traverseTree(root.left)
        right = self.traverseTree(root.right)

        self.is_balanced &= abs(left - right) < 2

        return max(left, right) + 1