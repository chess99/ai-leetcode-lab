# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        return sum(prefix[i + 1] - prefix[max(0, i - nums[i])] for i in range(len(nums)))
