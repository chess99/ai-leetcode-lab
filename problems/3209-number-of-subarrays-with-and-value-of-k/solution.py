# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        previous: list[tuple[int, int]] = []
        answer = 0

        for value in nums:
            current: list[tuple[int, int]] = [(value, 1)]
            for old_and, count in previous:
                new_and = old_and & value
                if current[-1][0] == new_and:
                    current[-1] = (new_and, current[-1][1] + count)
                else:
                    current.append((new_and, count))
            for and_value, count in current:
                if and_value == k:
                    answer += count
            previous = current

        return answer
