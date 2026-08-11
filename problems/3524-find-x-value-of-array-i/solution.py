# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        lurminexod = nums
        result = [0] * k
        ending = [0] * k
        for value in lurminexod:
            current = [0] * k
            current[value % k] = 1
            for remainder, count in enumerate(ending):
                current[(remainder * value) % k] += count
            for remainder in range(k):
                result[remainder] += current[remainder]
            ending = current
        return result
