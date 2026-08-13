# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:45:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        left, right = 0, len(records)
        while left < right:
            middle = (left + right) // 2
            if records[middle] == middle:
                left = middle + 1
            else:
                right = middle
        return left
