# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:17Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:return []
        queue=deque([root]);result=[]
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft();level.append(node.val);queue.extend(node.children)
            result.append(level)
        return result
