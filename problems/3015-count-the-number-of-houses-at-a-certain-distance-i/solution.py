# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        answer = [0] * n
        for first in range(1, n + 1):
            for second in range(first + 1, n + 1):
                distance = min(
                    second - first,
                    abs(first - x) + 1 + abs(second - y),
                    abs(first - y) + 1 + abs(second - x),
                )
                answer[distance - 1] += 2
        return answer
