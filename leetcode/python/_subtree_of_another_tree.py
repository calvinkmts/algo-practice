from lib2to3.fixes.fix_next import is_subtree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    is_subtree_found = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_subtree_found:
            return self.is_subtree_found

        self.is_subtree_found |= self.traverseTree(root, subRoot)

        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)

        return self.is_subtree_found

    def traverseTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.traverseTree(root.left, subRoot.left) and (self.traverseTree(root.right, subRoot.right))

