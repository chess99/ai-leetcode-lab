# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        positive_index = 0
        negative_index = 1
        for number in nums:
            if number > 0:
                answer[positive_index] = number
                positive_index += 2
            else:
                answer[negative_index] = number
                negative_index += 2
        return answer
