# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:09Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        difference = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            delta = 1 if direction else -1
            difference[start] += delta
            difference[end + 1] -= delta

        offset = 0
        result = []
        for index, char in enumerate(s):
            offset += difference[index]
            result.append(chr((ord(char) - ord('a') + offset) % 26 + ord('a')))
        return ''.join(result)
