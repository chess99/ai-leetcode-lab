# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def required_days(capacity: int) -> int:
            used_days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    used_days += 1
                    current_weight = 0
                current_weight += weight
            return used_days

        left, right = max(weights), sum(weights)
        while left < right:
            middle = (left + right) // 2
            if required_days(middle) <= days:
                right = middle
            else:
                left = middle + 1
        return left
