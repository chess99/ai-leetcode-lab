# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        limit = (1 << 31) - 1

        def next_larger(value):
            c = value
            zeros = ones = 0
            while c and c & 1 == 0:
                zeros += 1
                c >>= 1
            while c & 1:
                ones += 1
                c >>= 1
            position = zeros + ones
            if position >= 31 or position == 0:
                return -1
            value |= 1 << position
            value &= ~((1 << position) - 1)
            value |= (1 << (ones - 1)) - 1
            return value if value <= limit else -1

        def next_smaller(value):
            temporary = value
            ones = zeros = 0
            while temporary & 1:
                ones += 1
                temporary >>= 1
            if temporary == 0:
                return -1
            while temporary and temporary & 1 == 0:
                zeros += 1
                temporary >>= 1
            position = ones + zeros
            value &= ~((1 << (position + 1)) - 1)
            value |= ((1 << (ones + 1)) - 1) << (zeros - 1)
            return value

        return [next_larger(num), next_smaller(num)]
