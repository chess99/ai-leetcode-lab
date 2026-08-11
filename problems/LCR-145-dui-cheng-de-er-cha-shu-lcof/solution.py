# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:43:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        def mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left or not right:
                return left is right
            return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)

        return not root or mirror(root.left, root.right)
