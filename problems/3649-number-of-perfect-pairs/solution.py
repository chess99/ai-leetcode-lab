# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        jurnavalic = nums
        values = sorted(abs(value) for value in jurnavalic)
        answer = 0
        left = 0
        for right, value in enumerate(values):
            while left < right and value > 2 * values[left]:
                left += 1
            answer += right - left
        return answer
