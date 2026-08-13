# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:06:57Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val > root.val:
            return TreeNode(val, root)

        current = root
        while current.right and current.right.val > val:
            current = current.right
        current.right = TreeNode(val, current.right)
        return root
