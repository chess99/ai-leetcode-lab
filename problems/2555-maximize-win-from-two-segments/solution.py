# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        best_before = [0] * (n + 1)
        answer = left = 0
        for right, position in enumerate(prizePositions):
            while position - prizePositions[left] > k:
                left += 1
            current = right - left + 1
            answer = max(answer, current + best_before[left])
            best_before[right + 1] = max(best_before[right], current)
        return answer
