# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:15Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        locations = {value: index for index, value in enumerate(postorder)}
        def build(pre_left, pre_right, post_left, post_right):
            if pre_left > pre_right: return None
            root = TreeNode(preorder[pre_left])
            if pre_left == pre_right: return root
            split = locations[preorder[pre_left + 1]]
            left_size = split - post_left + 1
            root.left = build(pre_left + 1, pre_left + left_size, post_left, split)
            root.right = build(pre_left + left_size + 1, pre_right, split + 1, post_right - 1)
            return root
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
