# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        pairs = answer = left = 0
        for right, value in enumerate(nums):
            pairs += counts[value]
            counts[value] += 1
            while pairs >= k:
                answer += len(nums) - right
                counts[nums[left]] -= 1
                pairs -= counts[nums[left]]
                left += 1
        return answer
