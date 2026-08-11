# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        answer = length = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                length += 1
            else:
                length = 1
            answer += length
        return answer
