# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0: return False
        buckets = {}; width = valueDiff + 1
        for i, value in enumerate(nums):
            bucket = value // width
            if bucket in buckets or (bucket - 1 in buckets and value - buckets[bucket - 1] <= valueDiff) or (bucket + 1 in buckets and buckets[bucket + 1] - value <= valueDiff): return True
            buckets[bucket] = value
            if i >= indexDiff: del buckets[nums[i - indexDiff] // width]
        return False
