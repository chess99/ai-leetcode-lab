# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:30Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3:
            return []

        middle = num // 3
        return [middle - 1, middle, middle + 1]
