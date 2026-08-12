# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        tavelirnox = nums
        values = [value for value in tavelirnox if value >= 0]
        if not values:
            return tavelirnox
        shift = k % len(values)
        rotated = values[shift:] + values[:shift]
        iterator = iter(rotated)
        return [next(iterator) if value >= 0 else value for value in tavelirnox]
