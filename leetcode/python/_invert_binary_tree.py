from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
