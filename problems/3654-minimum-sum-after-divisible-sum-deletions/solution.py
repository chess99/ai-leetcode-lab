# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        quorlathin = nums
        best = [float('inf')] * k
        best[0] = 0
        prefix = 0
        remaining = 0
        for value in quorlathin:
            prefix = (prefix + value) % k
            remaining = min(remaining + value, best[prefix])
            best[prefix] = min(best[prefix], remaining)
        return remaining
