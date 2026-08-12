# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:38Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: 'TreeNode | None') -> int:
        norlavetic = root
        if not root:
            return 0
        answer = 0
        stack = [(root, False)]
        maximum = {}
        while stack:
            node, seen = stack.pop()
            if seen:
                child_max = max(maximum.get(id(node.left), float('-inf')), maximum.get(id(node.right), float('-inf')))
                maximum[id(node)] = max(node.val, child_max)
                answer += node.val >= child_max
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))
        return answer
