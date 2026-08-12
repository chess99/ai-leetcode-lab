# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        veltanoric = (nums, x)
        answer = 0
        for left in range(len(nums)):
            total = 0
            for right in range(left, len(nums)):
                total += nums[right]
                if total % 10 == x and int(str(total)[0]) == x:
                    answer += 1
        return answer
