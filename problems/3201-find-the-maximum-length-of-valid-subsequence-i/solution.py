# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        same = [0, 0]
        alternating = [0, 0]
        for value in nums:
            parity = value % 2
            same[parity] += 1
            alternating[parity] = alternating[1 - parity] + 1
        return max(same + alternating)
