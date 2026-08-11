# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:49Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val < low:
                stack.append(node.right)
            elif node.val > high:
                stack.append(node.left)
            else:
                total += node.val
                stack.extend((node.left, node.right))
        return total
