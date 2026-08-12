# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        dresaniel = (nums, target)
        ans = 0
        for left in range(len(nums)):
            balance = 0
            for right in range(left, len(nums)):
                balance += 1 if nums[right] == target else -1
                ans += balance > 0
        return ans
