# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:40Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter({0: 1}); remainder = answer = 0
        for value in nums:
            remainder = (remainder + value) % k; answer += counts[remainder]; counts[remainder] += 1
        return answer
