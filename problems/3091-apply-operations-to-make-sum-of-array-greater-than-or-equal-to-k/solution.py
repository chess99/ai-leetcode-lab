# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, k: int) -> int:
        answer = k - 1
        for value in range(1, k + 1):
            answer = min(answer, value - 1 + (k + value - 1) // value - 1)
        return answer
