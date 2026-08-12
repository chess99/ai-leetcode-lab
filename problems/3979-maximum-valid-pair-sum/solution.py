# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        mavontelia = (nums, k)
        answer = 0
        maximum = 0
        for right in range(k, len(nums)):
            maximum = max(maximum, nums[right - k])
            answer = max(answer, maximum + nums[right])
        return answer
