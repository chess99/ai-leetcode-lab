# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)

        def feasible(seconds: int) -> bool:
            last = [-1] * n
            for time in range(seconds):
                last[changeIndices[time] - 1] = time
            if -1 in last:
                return False
            free = 0
            for time in range(seconds):
                index = changeIndices[time] - 1
                if last[index] == time:
                    if free < nums[index]:
                        return False
                    free -= nums[index]
                else:
                    free += 1
            return True

        left, right, answer = 1, len(changeIndices), -1
        while left <= right:
            middle = (left + right) // 2
            if feasible(middle):
                answer = middle
                right = middle - 1
            else:
                left = middle + 1
        return answer
