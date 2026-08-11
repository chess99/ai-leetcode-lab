# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        answer = 0
        for source, target in zip(s, t):
            a, b = ord(source) - 97, ord(target) - 97
            forward = sum(nextCost[(a + step) % 26] for step in range((b - a) % 26))
            backward = sum(previousCost[(a - step) % 26] for step in range((a - b) % 26))
            answer += min(forward, backward)
        return answer
