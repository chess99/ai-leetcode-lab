# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        modulus = 10 ** 9 + 7
        if sum(nums) < 2 * k:
            return 0
        dynamic = [0] * k
        dynamic[0] = 1
        for value in nums:
            for total in range(k - 1, value - 1, -1):
                dynamic[total] = (dynamic[total] + dynamic[total - value]) % modulus
        return (pow(2, len(nums), modulus) - 2 * sum(dynamic)) % modulus
