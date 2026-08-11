# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        prefix_sum = 0
        count = 0
        for number in nums:
            prefix_sum += number
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1
        return count
