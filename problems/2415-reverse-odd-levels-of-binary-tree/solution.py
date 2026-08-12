# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:15Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from collections import deque
from typing import Optional
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root]); level = 0
        while queue:
            nodes = list(queue)
            if level % 2:
                for index in range(len(nodes) // 2):
                    nodes[index].val, nodes[-1 - index].val = nodes[-1 - index].val, nodes[index].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.extend((node.left, node.right))
            level += 1
        return root
