# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True] * (right + 1)
        if right >= 0: prime[0] = False
        if right >= 1: prime[1] = False
        for d in range(2, int(right ** 0.5) + 1):
            if prime[d]:
                prime[d * d:right + 1:d] = [False] * (((right - d * d) // d) + 1)
        previous, answer, best = -1, [-1, -1], float('inf')
        for value in range(max(2, left), right + 1):
            if prime[value]:
                if previous != -1 and value - previous < best:
                    answer, best = [previous, value], value - previous
                previous = value
        return answer
