# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        right = Counter(nums); left = Counter(); answer = 0
        for value in nums:
            right[value] -= 1
            answer = (answer + left[2 * value] * right[2 * value]) % mod
            left[value] += 1
        return answer
