# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    final_solution: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.traverseTree(root.left) + self.traverseTree(root.right), self.final_solution)

    def traverseTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.traverseTree(root.left)
        right = self.traverseTree(root.right)

        self.final_solution = max(self.final_solution, left + right)

        return max(left, right) + 1
