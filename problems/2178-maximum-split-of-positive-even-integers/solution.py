# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:31Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []

        answer = []
        next_value = 2
        while finalSum >= next_value:
            answer.append(next_value)
            finalSum -= next_value
            next_value += 2

        if finalSum:
            answer[-1] += finalSum
        return answer
