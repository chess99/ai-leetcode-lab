# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:16Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize=None)
        def build(size):
            if size == 1: return (TreeNode(0),)
            if size % 2 == 0: return ()
            result = []
            for left_size in range(1, size, 2):
                for left in build(left_size):
                    for right in build(size - left_size - 1): result.append(TreeNode(0, left, right))
            return tuple(result)
        return list(build(n))
