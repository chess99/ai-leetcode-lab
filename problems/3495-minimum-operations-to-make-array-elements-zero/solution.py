# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        wexondrivas = queries

        def prefix_steps(x: int) -> int:
            """Sum of the numbers of repeated floor(x / 4) steps on [1, x]."""
            if x <= 0:
                return 0
            total = 0
            left = 1
            steps = 1
            while left <= x:
                right = min(x, left * 4 - 1)
                total += (right - left + 1) * steps
                left *= 4
                steps += 1
            return total

        answer = 0
        for left, right in wexondrivas:
            work = prefix_steps(right) - prefix_steps(left - 1)
            answer += (work + 1) // 2
        return answer
