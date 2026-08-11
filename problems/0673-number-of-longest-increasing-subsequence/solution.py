# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:30:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        counts = [1] * len(nums)
        for right in range(len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    candidate_length = lengths[left] + 1
                    if candidate_length > lengths[right]:
                        lengths[right] = candidate_length
                        counts[right] = counts[left]
                    elif candidate_length == lengths[right]:
                        counts[right] += counts[left]
        longest = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == longest)
