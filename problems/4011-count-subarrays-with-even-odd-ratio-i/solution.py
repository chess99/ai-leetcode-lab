# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        norvelith = (nums, a, b)
        answer = 0
        for left in range(len(nums)):
            even = odd = 0
            for value in nums[left:]:
                if value & 1: odd += 1
                else: even += 1
                answer += odd > 0 and even * b <= odd * a
        return answer
