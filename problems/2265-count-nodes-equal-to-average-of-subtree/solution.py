# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:21Z
# Experiment: ai-leetcode-lab, round 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        totals = {}
        matches = 0
        stack = [(root, False)]

        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if not expanded:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            left_sum, left_count = totals.get(node.left, (0, 0))
            right_sum, right_count = totals.get(node.right, (0, 0))
            total = left_sum + node.val + right_sum
            count = left_count + 1 + right_count
            if node.val == total // count:
                matches += 1
            totals[node] = (total, count)

        return matches
