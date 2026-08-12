# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bravendil = nums
        magnitudes = sorted(abs(value) for value in nums)
        return 100_000 * magnitudes[-1] * magnitudes[-2]
