# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k

        def place(index: int) -> bool:
            if index == len(nums):
                return True
            value = nums[index]
            for bucket in range(k):
                if buckets[bucket] + value > target:
                    continue
                buckets[bucket] += value
                if place(index + 1):
                    return True
                buckets[bucket] -= value
                if buckets[bucket] == 0:
                    break
            return False

        return place(0)
