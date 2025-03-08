# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.left
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.right
            else:
                return cur


    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return root
    #
    #     if root.val == p.val or root.val == q.val:
    #         return root
    #
    #     # find p and q on both side of the root
    #     is_p_on_left = self.findNode(root.left, p)
    #     is_q_on_left = self.findNode(root.left, q)
    #
    #     is_p_on_right = self.findNode(root.right, p)
    #     is_q_on_right = self.findNode(root.right, q)
    #
    #     found_on_left = is_p_on_left or is_q_on_left
    #     found_on_right = is_p_on_right or is_q_on_right
    #
    #     if found_on_right and found_on_left:
    #         return root
    #
    #     if found_on_left:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #
    #     if found_on_right:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #
    #
    # def findNode(self, root: 'TreeNode', node: 'TreeNode') -> bool:
    #     if not root:
    #         return False
    #
    #     if root.val == node.val:
    #         return True
    #
    #     return self.findNode(root.left, node) or self.findNode(root.right, node)