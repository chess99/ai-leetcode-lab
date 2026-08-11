# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left = answer = 0
        for value in nums:
            if value == 0:
                right = total - left
                if left == right:
                    answer += 2
                elif abs(left - right) == 1:
                    answer += 1
            left += value
        return answer
