# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = 0; stack = [(root, 0)]
        while stack:
            node, mask = stack.pop(); mask ^= 1 << node.val
            if node.left is None and node.right is None: count += mask & (mask - 1) == 0
            if node.left: stack.append((node.left, mask))
            if node.right: stack.append((node.right, mask))
        return count
