# AI solution attribution
from typing import Optional
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:52Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional['TreeNode']) -> int:
        answer = 0
        information = {}
        stack = [(root, False)] if root else []
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                continue
            left = information.get(node.left, (True, float('inf'), float('-inf'), 0))
            right = information.get(node.right, (True, float('inf'), float('-inf'), 0))
            if left[0] and right[0] and left[2] < node.val < right[1]:
                total = left[3] + node.val + right[3]
                answer = max(answer, total)
                information[node] = (True, min(left[1], node.val),
                                     max(right[2], node.val), total)
            else:
                information[node] = (False, 0, 0, 0)
        return answer
