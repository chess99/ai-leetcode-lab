# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        first_seen = {}
        score = 0
        answer = 0
        for index, hour in enumerate(hours):
            score += 1 if hour > 8 else -1
            if score > 0:
                answer = index + 1
            elif score - 1 in first_seen:
                answer = max(answer, index - first_seen[score - 1])
            first_seen.setdefault(score, index)
        return answer
