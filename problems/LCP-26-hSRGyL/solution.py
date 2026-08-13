# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:46Z
# Experiment: ai-leetcode-lab, round 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def navigation(self, root: TreeNode) -> int:
        graph = {}
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            graph.setdefault(node, [])
            if parent is not None:
                graph[node].append(parent)
                graph[parent].append(node)
            if node.left is not None:
                stack.append((node.left, node))
            if node.right is not None:
                stack.append((node.right, node))

        major_vertices = [node for node, neighbors in graph.items() if len(neighbors) >= 3]
        if not major_vertices:
            return 1

        leaves = sum(len(neighbors) == 1 for neighbors in graph.values())
        exterior_major = 0
        for major in major_vertices:
            has_terminal_leaf = False
            for neighbor in graph[major]:
                previous, current = major, neighbor
                while len(graph[current]) == 2:
                    first, second = graph[current]
                    previous, current = current, second if first is previous else first
                if len(graph[current]) == 1:
                    has_terminal_leaf = True
                    break
            exterior_major += has_terminal_leaf
        return leaves - exterior_major
