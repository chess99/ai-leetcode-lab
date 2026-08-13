# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:52Z
# Experiment: ai-leetcode-lab, round 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [[root, 0, None]]
        result = None
        while stack:
            node, state, left_result = stack[-1]
            if state == 0:
                if node is p or node is q:
                    result = node
                    stack.pop()
                    continue
                stack[-1][1] = 1
                if node.left:
                    stack.append([node.left, 0, None])
                else:
                    result = None
            elif state == 1:
                stack[-1][1] = 2
                stack[-1][2] = result
                if node.right:
                    stack.append([node.right, 0, None])
                else:
                    result = None
            else:
                right_result = result
                if left_result and right_result:
                    result = node
                else:
                    result = left_result or right_result
                stack.pop()
        return result
