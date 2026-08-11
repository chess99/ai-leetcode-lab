# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []

        for number in nums:
            if number < pivot:
                smaller.append(number)
            elif number == pivot:
                equal.append(number)
            else:
                greater.append(number)

        return smaller + equal + greater
