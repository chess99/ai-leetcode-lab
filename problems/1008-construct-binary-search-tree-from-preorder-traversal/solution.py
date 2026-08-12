# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:08:50Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index=0
        def build(bound):
            nonlocal index
            if index==len(preorder) or preorder[index]>bound:return None
            node=TreeNode(preorder[index]);index+=1
            node.left=build(node.val);node.right=build(bound)
            return node
        return build(float('inf'))
