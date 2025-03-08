import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            q_length = len(q)
            temp_result = []

            for i in range(q_length):
                node = q.popleft()
                if node:
                    temp_result.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if temp_result:
                res.append(temp_result)

        return res


    # q: List[List[int]] = []
    #
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     q = []
    #
    #     self.traverseTree(root, 1)
    #
    #     return self.q
    #
    # def traverseTree(self, root: Optional[TreeNode], level: int) -> None:
    #     if not root:
    #         return None
    #
    #     print(len(self.q), level)
    #
    #     if len(self.q) < level:
    #         self.q.append([root.val])
    #     else:
    #         self.q[level-1].append(root.val)
    #
    #     self.traverseTree(root.left, level+1)
    #     self.traverseTree(root.right, level+1)
    #
    #     return None