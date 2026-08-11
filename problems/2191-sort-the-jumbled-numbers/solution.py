# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(number: int) -> int:
            if number == 0:
                return mapping[0]
            digits = []
            while number:
                digits.append(str(mapping[number % 10]))
                number //= 10
            return int(''.join(reversed(digits)))

        return sorted(nums, key=mapped_value)
