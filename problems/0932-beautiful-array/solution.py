# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]
        while len(result) < n:
            result = [2 * value - 1 for value in result if 2 * value - 1 <= n] + \
                     [2 * value for value in result if 2 * value <= n]
        return result
