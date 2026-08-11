# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1
        return result
