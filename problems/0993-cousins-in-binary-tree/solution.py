# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:21:20Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, None)]
        while queue:
            next_level, found = [], {}
            for node, parent in queue:
                if node.val in (x, y): found[node.val] = parent
                if node.left: next_level.append((node.left, node))
                if node.right: next_level.append((node.right, node))
            if len(found) == 2: return found[x] is not found[y]
            if found: return False
            queue = next_level
        return False
