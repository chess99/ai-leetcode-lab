# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        modulus = 1_000_000_007
        size = len(nums)
        maximum = max(nums)
        total = sum(nums)

        if size <= 2 or cost2 >= 2 * cost1:
            return ((size * maximum - total) * cost1) % modulus

        minimum = min(nums)
        threshold = (total - 2 * minimum + size - 3) // (size - 2)

        def cost(target):
            missing = size * target - total
            largest_gap = target - minimum
            pairs = min(missing // 2, missing - largest_gap)
            singles = missing - 2 * pairs
            return pairs * cost2 + singles * cost1

        candidates = {maximum, maximum + 1}
        for target in range(threshold - 1, threshold + 2):
            if target >= maximum:
                candidates.add(target)
        return min(cost(target) for target in candidates) % modulus
