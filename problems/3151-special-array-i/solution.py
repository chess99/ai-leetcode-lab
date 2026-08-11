# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((nums[i - 1] + nums[i]) % 2 == 1 for i in range(1, len(nums)))
