# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:56:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}; prefix = answer = 0
        for value in nums:
            prefix += value
            if prefix - target in seen:
                answer += 1; prefix = 0; seen = {0}
            else: seen.add(prefix)
        return answer
