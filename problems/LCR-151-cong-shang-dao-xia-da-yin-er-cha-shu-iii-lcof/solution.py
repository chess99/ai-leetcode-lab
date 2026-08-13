# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:34Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, answer, reverse = deque([root]), [], False
        while queue:
            level = [queue.popleft() for _ in range(len(queue))]
            values = [node.val for node in level]
            if reverse: values.reverse()
            answer.append(values); reverse = not reverse
            for node in level:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return answer
