# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:00:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        answer = 0
        for index, value in enumerate(nums):
            left_valid = index < k or value > nums[index - k]
            right_valid = index + k >= len(nums) or value > nums[index + k]
            if left_valid and right_valid:
                answer += value
        return answer
