# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:39Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs = 0
        def dfs(node):
            nonlocal pairs
            if not node: return []
            if not node.left and not node.right: return [1]
            left, right = dfs(node.left), dfs(node.right)
            pairs += sum(a + b <= distance for a in left for b in right)
            return [steps + 1 for steps in left + right if steps + 1 < distance]
        dfs(root); return pairs
