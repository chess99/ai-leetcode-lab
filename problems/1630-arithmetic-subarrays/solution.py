# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        answer = []
        for start, end in zip(l, r):
            values = sorted(nums[start : end + 1])
            difference = values[1] - values[0]
            answer.append(
                all(values[index] - values[index - 1] == difference for index in range(2, len(values)))
            )
        return answer
