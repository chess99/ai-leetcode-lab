# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:51Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack=[]; previous=None; answer=float('inf')
        while stack or root:
            while root: stack.append(root); root=root.left
            root=stack.pop()
            if previous is not None: answer=min(answer,root.val-previous)
            previous=root.val; root=root.right
        return answer
