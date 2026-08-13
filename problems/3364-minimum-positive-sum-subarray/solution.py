# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")
        for start in range(len(nums)):
            total = 0
            for end in range(start, min(len(nums), start + r)):
                total += nums[end]
                if end - start + 1 >= l and total > 0:
                    answer = min(answer, total)
        return answer if answer != float("inf") else -1
