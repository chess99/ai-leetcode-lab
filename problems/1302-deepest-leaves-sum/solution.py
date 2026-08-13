# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:20Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
from collections import deque
from typing import Optional
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft(); total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return total
