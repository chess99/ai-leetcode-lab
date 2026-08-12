# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        answer = 0
        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                extensions = dp[left][difference]
                answer += extensions
                dp[right][difference] += extensions + 1
        return answer
