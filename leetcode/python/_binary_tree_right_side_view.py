# Definition for a binary tree node.
import collections
from http.cookiejar import cut_port_re
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            q_length = len(q)
            current_level = []

            for i in range(q_length):
                node = q.popleft()
                if node:
                    current_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if current_level:
                result.append(current_level[-1])

        return result


