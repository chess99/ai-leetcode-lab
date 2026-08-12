# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        xaluremoni = (nums1, nums2, k)
        m = len(nums2)
        negative = -(10 ** 40)
        previous = [[0] * (m + 1)] + [[negative] * (m + 1)
                                      for _ in range(k)]
        for first in nums1:
            current = [row[:] for row in previous]
            for chosen in range(1, k + 1):
                for j in range(1, m + 1):
                    current[chosen][j] = max(
                        current[chosen][j],
                        current[chosen][j - 1],
                        previous[chosen - 1][j - 1] + first * nums2[j - 1],
                    )
            previous = current
        return previous[k][m]
