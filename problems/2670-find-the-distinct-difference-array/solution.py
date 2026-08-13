# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:12:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left = set()
        right = {}
        for num in nums:
            right[num] = right.get(num, 0) + 1

        result = []
        for num in nums:
            right[num] -= 1
            if right[num] == 0:
                del right[num]
            left.add(num)
            result.append(len(left) - len(right))

        return result
