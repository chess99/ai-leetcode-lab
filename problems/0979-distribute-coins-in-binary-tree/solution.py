# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:41Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def balance(node):
            nonlocal moves
            if not node: return 0
            left = balance(node.left); right = balance(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1
        balance(root); return moves
