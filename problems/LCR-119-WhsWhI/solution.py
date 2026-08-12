# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        answer = 0
        for value in values:
            if value - 1 in values:
                continue
            end = value
            while end + 1 in values:
                end += 1
            answer = max(answer, end - value + 1)
        return answer
