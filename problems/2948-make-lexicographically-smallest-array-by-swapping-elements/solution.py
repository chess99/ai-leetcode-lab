# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = sorted((value, i) for i, value in enumerate(nums))
        for start in range(len(nums)):
            if start and pairs[start][0] - pairs[start - 1][0] <= limit:
                continue
            end = start + 1
            while end < len(nums) and pairs[end][0] - pairs[end - 1][0] <= limit:
                end += 1
            indices = sorted(i for _, i in pairs[start:end])
            for i, (value, _) in zip(indices, pairs[start:end]):
                nums[i] = value
        return nums
