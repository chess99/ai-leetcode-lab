# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:42:13Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closest_pair(value: int) -> List[int]:
            factor = isqrt(value)
            while value % factor:
                factor -= 1
            return [factor, value // factor]

        first = closest_pair(num + 1)
        second = closest_pair(num + 2)
        return first if first[1] - first[0] <= second[1] - second[0] else second
