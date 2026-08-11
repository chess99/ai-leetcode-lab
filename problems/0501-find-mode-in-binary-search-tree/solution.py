# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:39:54Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
        previous = None
        count = maximum = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val == previous:
                count += 1
            else:
                previous = node.val
                count = 1
            if count > maximum:
                maximum = count
                result = [node.val]
            elif count == maximum:
                result.append(node.val)
            node = node.right
        return result
