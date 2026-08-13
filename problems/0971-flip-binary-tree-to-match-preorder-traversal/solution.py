# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional
# Definition for a binary tree node.
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        index = 0; flips = []
        def walk(node):
            nonlocal index
            if not node: return True
            if index == len(voyage) or node.val != voyage[index]: return False
            index += 1
            if node.left and index < len(voyage) and node.left.val != voyage[index]: flips.append(node.val); node.left, node.right = node.right, node.left
            return walk(node.left) and walk(node.right)
        return flips if walk(root) else [-1]
