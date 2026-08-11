# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:23Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        non_increasing = [0] * length
        non_decreasing = [0] * length

        for index in range(1, length):
            if security[index - 1] >= security[index]:
                non_increasing[index] = non_increasing[index - 1] + 1

        for index in range(length - 2, -1, -1):
            if security[index] <= security[index + 1]:
                non_decreasing[index] = non_decreasing[index + 1] + 1

        return [
            index
            for index in range(length)
            if non_increasing[index] >= time and non_decreasing[index] >= time
        ]
