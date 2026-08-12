# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:45Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def solve(position: int) -> int:
            if position <= 1:
                return position * inc
            answer = position * inc
            for distance, fare in zip(jump, cost):
                quotient, remainder = divmod(position, distance)
                answer = min(answer, solve(quotient) + fare + remainder * inc)
                if remainder and quotient + 1 < position:
                    answer = min(
                        answer,
                        solve(quotient + 1) + fare + (distance - remainder) * dec,
                    )
            return answer

        return solve(target) % mod
