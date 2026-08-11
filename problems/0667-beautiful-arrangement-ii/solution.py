# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            result.append(left)
            left += 1
            if left <= right:
                result.append(right)
                right -= 1
        return result
