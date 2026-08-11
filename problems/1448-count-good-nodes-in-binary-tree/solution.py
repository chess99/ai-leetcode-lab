# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:29Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node,maximum):
            if not node:return 0
            good=node.val>=maximum
            return good+dfs(node.left,max(maximum,node.val))+dfs(node.right,max(maximum,node.val))
        return dfs(root,float('-inf'))
