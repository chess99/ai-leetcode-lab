# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        answer = 10 ** 18
        previous = set()
        for value in nums:
            current = {value}
            current.update(previous_value | value for previous_value in previous)
            answer = min(answer, *(abs(candidate - k) for candidate in current))
            if answer == 0:
                return 0
            previous = current
        return answer
