# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:33Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_counts = Counter(number % k for number in arr)

        if remainder_counts[0] % 2 != 0:
            return False

        for remainder in range(1, (k // 2) + 1):
            complement = k - remainder
            if remainder == complement:
                if remainder_counts[remainder] % 2 != 0:
                    return False
            elif remainder_counts[remainder] != remainder_counts[complement]:
                return False

        return True
