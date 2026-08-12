# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:50Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        velantris = (nums, k)
        remainder_count = {0: 1}
        prefix = 0
        answer = 0
        for value in nums:
            prefix = (prefix + value) % k
            answer += remainder_count.get(prefix, 0)
            remainder_count[prefix] = remainder_count.get(prefix, 0) + 1

        start = 0
        while start < len(nums):
            end = start + 1
            while end < len(nums) and nums[end] == nums[start]:
                end += 1
            count = end - start
            period = k // gcd(k, nums[start])
            multiples = count // period
            answer -= multiples * count - period * multiples * (multiples + 1) // 2
            start = end
        return answer
