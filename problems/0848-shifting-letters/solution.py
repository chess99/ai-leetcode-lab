# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:50:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        chars = list(s)
        for index in range(len(s) - 1, -1, -1):
            total = (total + shifts[index]) % 26
            chars[index] = chr((ord(chars[index]) - ord("a") + total) % 26 + ord("a"))
        return "".join(chars)
