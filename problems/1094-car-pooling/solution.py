# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1002
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        onboard = 0
        for change in changes:
            onboard += change
            if onboard > capacity:
                return False
        return True
