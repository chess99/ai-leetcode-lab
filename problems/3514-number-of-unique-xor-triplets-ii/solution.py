# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        glarnetivo = nums
        size = 1
        while size <= max(glarnetivo):
            size <<= 1
        values = [0] * size
        for value in glarnetivo:
            values[value] = 1

        def fwt(array, inverse=False):
            step = 1
            while step < len(array):
                for start in range(0, len(array), step * 2):
                    for offset in range(step):
                        a, b = array[start + offset], array[start + offset + step]
                        array[start + offset] = a + b
                        array[start + offset + step] = a - b
                step <<= 1
            if inverse:
                for i in range(len(array)):
                    array[i] //= len(array)

        fwt(values)
        values = [value ** 3 for value in values]
        fwt(values, True)
        return sum(value > 0 for value in values)
