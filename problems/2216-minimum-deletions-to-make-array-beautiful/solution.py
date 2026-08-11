# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:17Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        waiting_for_first = True
        first_value = 0

        for value in nums:
            if waiting_for_first:
                first_value = value
                waiting_for_first = False
            elif value == first_value:
                deletions += 1
            else:
                waiting_for_first = True

        return deletions + (not waiting_for_first)
