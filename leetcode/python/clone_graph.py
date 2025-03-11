# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}
        def clone_node(node: Node):
            if node in node_map:
                return node_map[node]

            new_node = Node(val=node.val)

            node_map[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(clone_node(neighbor))

            return new_node

        return clone_node(node)