# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:07Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
# Definition for a binary tree node.
from typing import Optional
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(node, link):
            if not link: return True
            if not node or node.val != link.val: return False
            return match(node.left, link.next) or match(node.right, link.next)
        if not root: return False
        return match(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
