# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:20Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
from typing import List, Optional
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            stack, values = [], []
            while stack or root:
                while root: stack.append(root); root = root.left
                root = stack.pop(); values.append(root.val); root = root.right
            return values
        first, second = inorder(root1), inorder(root2)
        answer = []; i = j = 0
        while i < len(first) and j < len(second):
            if first[i] <= second[j]: answer.append(first[i]); i += 1
            else: answer.append(second[j]); j += 1
        return answer + first[i:] + second[j:]
