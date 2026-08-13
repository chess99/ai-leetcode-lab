# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:43:02Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        level = [root]
        while level:
            result.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return result
