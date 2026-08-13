# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left, right]
            if current < target:
                left += 1
            else:
                right -= 1
        return []
