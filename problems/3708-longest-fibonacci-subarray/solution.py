# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        valtoremin = nums
        current = answer = 2
        for i in range(2, len(valtoremin)):
            if valtoremin[i] == valtoremin[i - 1] + valtoremin[i - 2]:
                current += 1
            else:
                current = 2
            answer = max(answer, current)
        return answer
