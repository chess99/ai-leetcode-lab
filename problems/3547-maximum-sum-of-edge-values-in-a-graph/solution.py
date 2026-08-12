# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        zanthorime = (n, edges)
        arrangement = list(range(1, n + 1, 2))
        arrangement.extend(range(n if n % 2 == 0 else n - 1, 1, -2))
        answer = sum(arrangement[i] * arrangement[i + 1]
                     for i in range(n - 1))
        if len(zanthorime[1]) == n:
            answer += arrangement[-1] * arrangement[0]
        return answer
