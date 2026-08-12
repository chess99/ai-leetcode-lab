# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        reachable = 1
        for value in sorted(set(rewardValues)):
            reachable |= (reachable & ((1 << value) - 1)) << value
        return reachable.bit_length() - 1
