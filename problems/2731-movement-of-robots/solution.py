# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        positions = sorted(value + (d if direction == "R" else -d) for value, direction in zip(nums, s))
        prefix = answer = 0
        for index, position in enumerate(positions):
            answer += position * index - prefix
            prefix += position
        return answer % 1_000_000_007
