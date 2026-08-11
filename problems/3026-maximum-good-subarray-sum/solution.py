# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import Dict, List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        minimum_prefix: Dict[int, int] = {}
        prefix = 0
        answer = None
        for value in nums:
            for target in (value - k, value + k):
                if target in minimum_prefix:
                    candidate = prefix + value - minimum_prefix[target]
                    answer = candidate if answer is None else max(answer, candidate)
            minimum_prefix[value] = min(minimum_prefix.get(value, prefix), prefix)
            prefix += value
        return answer if answer is not None else 0
