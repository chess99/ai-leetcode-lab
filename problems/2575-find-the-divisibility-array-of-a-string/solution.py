# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remainder = 0
        answer = []
        for digit in word:
            remainder = (remainder * 10 + int(digit)) % m
            answer.append(int(remainder == 0))
        return answer
