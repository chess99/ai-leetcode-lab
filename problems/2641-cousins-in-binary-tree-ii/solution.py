# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional




class Solution:
    def replaceValueInTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        root.val = 0; level = [root]
        while level:
            total = sum(child.val for node in level for child in (node.left, node.right) if child)
            nxt = []
            for node in level:
                siblings = sum(child.val for child in (node.left, node.right) if child)
                for child in (node.left, node.right):
                    if child: child.val = total - siblings; nxt.append(child)
            level = nxt
        return root
