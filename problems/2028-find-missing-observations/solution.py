# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum = mean * (len(rolls) + n) - sum(rolls)
        if missing_sum < n or missing_sum > 6 * n:
            return []

        base, remainder = divmod(missing_sum, n)
        return [base + 1] * remainder + [base] * (n - remainder)
