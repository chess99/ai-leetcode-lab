# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:13Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxValue(self, root: 'TreeNode', k: int) -> int:
        stack = [(root, False)]
        dp = {}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            left = dp.get(id(node.left), [0] + [-10 ** 30] * k)
            right = dp.get(id(node.right), [0] + [-10 ** 30] * k)
            current = [-10 ** 30] * (k + 1)
            current[0] = max(left) + max(right)
            for left_size in range(k):
                for right_size in range(k - left_size):
                    size = 1 + left_size + right_size
                    current[size] = max(
                        current[size],
                        node.val + left[left_size] + right[right_size],
                    )
            dp[id(node)] = current
        return max(dp[id(root)])
