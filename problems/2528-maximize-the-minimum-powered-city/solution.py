# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        size = len(stations)
        prefix = [0]
        for value in stations:
            prefix.append(prefix[-1] + value)
        power = [
            prefix[min(size, index + r + 1)] - prefix[max(0, index - r)]
            for index in range(size)
        ]

        def feasible(target):
            difference = [0] * (size + 1)
            active = 0
            used = 0
            for index in range(size):
                active += difference[index]
                needed = max(0, target - power[index] - active)
                used += needed
                if used > k:
                    return False
                active += needed
                expiration = min(size, index + 2 * r + 1)
                difference[expiration] -= needed
            return True

        low = min(power)
        high = low + k
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
