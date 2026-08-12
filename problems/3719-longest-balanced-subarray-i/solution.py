# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        tavernilo = nums
        ans = 0
        for left in range(len(nums)):
            even, odd = set(), set()
            for right in range(left, len(nums)):
                (even if nums[right] % 2 == 0 else odd).add(nums[right])
                if len(even) == len(odd): ans = max(ans, right - left + 1)
        return ans
