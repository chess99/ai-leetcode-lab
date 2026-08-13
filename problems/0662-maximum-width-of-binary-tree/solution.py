# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, 0)])
        maximum = 0
        while queue:
            first_position = queue[0][1]
            maximum = max(maximum, queue[-1][1] - first_position + 1)
            for _ in range(len(queue)):
                node, position = queue.popleft()
                position -= first_position
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))

        return maximum
