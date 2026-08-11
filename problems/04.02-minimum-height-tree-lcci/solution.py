# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:57:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node

        return build(0, len(nums) - 1)
