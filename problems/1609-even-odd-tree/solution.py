# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:24Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
from collections import deque
from typing import Optional
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root]);level=0
        while queue:
            previous=float('-inf') if level%2==0 else float('inf')
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.val%2==level%2 or (level%2==0 and node.val<=previous) or (level%2 and node.val>=previous):return False
                previous=node.val
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            level+=1
        return True
