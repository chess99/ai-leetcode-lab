# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:31:38Z
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result, level = [], [root]
        while level:
            result.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]
        return result
