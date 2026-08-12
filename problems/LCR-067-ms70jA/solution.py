# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        mask = 0
        for bit in range(30, -1, -1):
            mask |= 1 << bit
            prefixes = {number & mask for number in nums}
            candidate = answer | (1 << bit)
            if any((prefix ^ candidate) in prefixes for prefix in prefixes):
                answer = candidate
        return answer
