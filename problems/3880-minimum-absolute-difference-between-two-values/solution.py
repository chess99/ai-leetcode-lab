# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:19:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last_one = -1
        last_two = -1
        answer = float('inf')

        for index, value in enumerate(nums):
            if value == 1:
                last_one = index
                if last_two != -1:
                    answer = min(answer, index - last_two)
            elif value == 2:
                last_two = index
                if last_one != -1:
                    answer = min(answer, index - last_one)

        return -1 if answer == float('inf') else answer
