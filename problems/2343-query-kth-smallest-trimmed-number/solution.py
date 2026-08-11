# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:28Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []

        for rank, trim in queries:
            ordered = sorted(range(len(nums)), key=lambda index: (nums[index][-trim:], index))
            answer.append(ordered[rank - 1])

        return answer
