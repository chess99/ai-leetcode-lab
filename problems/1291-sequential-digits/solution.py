# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        for length in range(2, 10):
            for start in range(10 - length):
                value = int(digits[start:start + length])
                if low <= value <= high:
                    result.append(value)
        return result
