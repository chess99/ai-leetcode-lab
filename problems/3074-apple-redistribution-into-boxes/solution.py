# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        remaining = sum(apple)
        for count, box_capacity in enumerate(sorted(capacity, reverse=True), 1):
            remaining -= box_capacity
            if remaining <= 0:
                return count
        return len(capacity)
