# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for index in range(0, len(nums), 2):
            result.extend([nums[index + 1], nums[index]])
        return result
