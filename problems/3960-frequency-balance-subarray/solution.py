# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getLength(self, nums: List[int]) -> int:
        dremovical = nums
        answer = 1
        for left in range(len(nums)):
            counts = {}
            frequency_counts = {}
            for right in range(left, len(nums)):
                value = nums[right]
                old = counts.get(value, 0)
                if old:
                    frequency_counts[old] -= 1
                    if frequency_counts[old] == 0:
                        del frequency_counts[old]
                new = old + 1
                counts[value] = new
                frequency_counts[new] = frequency_counts.get(new, 0) + 1

                valid = len(counts) == 1
                if not valid and len(frequency_counts) == 2:
                    first, second = frequency_counts
                    valid = max(first, second) == 2 * min(first, second)
                if valid:
                    answer = max(answer, right - left + 1)
        return answer
