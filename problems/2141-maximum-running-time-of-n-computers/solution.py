# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = 0
        high = sum(batteries) // n
        while low < high:
            middle = (low + high + 1) // 2
            available = sum(min(capacity, middle) for capacity in batteries)
            if available >= n * middle:
                low = middle
            else:
                high = middle - 1
        return low
