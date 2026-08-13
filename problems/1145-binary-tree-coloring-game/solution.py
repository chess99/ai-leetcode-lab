# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:24:05Z
# Experiment: ai-leetcode-lab, round 1

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        target_parts = (0, 0)

        def count(node: TreeNode) -> int:
            nonlocal target_parts
            if node is None:
                return 0
            left = count(node.left)
            right = count(node.right)
            if node.val == x:
                target_parts = (left, right)
            return left + right + 1

        count(root)
        left, right = target_parts
        return max(left, right, n - left - right - 1) > n // 2
