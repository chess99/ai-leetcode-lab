# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:09Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for index in range(1, len(nums)):
            difference = nums[index] - nums[0]
            if difference <= 0 or difference % 2:
                continue

            counts = Counter(nums)
            recovered = []
            valid = True
            for lower in nums:
                if counts[lower] == 0:
                    continue
                higher = lower + difference
                if counts[higher] == 0:
                    valid = False
                    break
                counts[lower] -= 1
                counts[higher] -= 1
                recovered.append(lower + difference // 2)

            if valid:
                return recovered
        return []
