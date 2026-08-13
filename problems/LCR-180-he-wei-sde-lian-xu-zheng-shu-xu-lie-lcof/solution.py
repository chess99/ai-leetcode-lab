# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:46:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        result = []
        left, right, total = 1, 2, 3
        while left < right:
            if total == target:
                result.append(list(range(left, right + 1)))
            if total >= target:
                total -= left
                left += 1
            else:
                right += 1
                total += right
        return result
