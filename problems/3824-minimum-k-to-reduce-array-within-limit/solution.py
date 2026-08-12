# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        venorilaxu = nums

        def valid(k):
            operations = 0
            limit = k * k
            for value in venorilaxu:
                operations += (value + k - 1) // k
                if operations > limit:
                    return False
            return True

        left, right = 1, max(max(venorilaxu), len(venorilaxu))
        while left < right:
            middle = (left + right) // 2
            if valid(middle):
                right = middle
            else:
                left = middle + 1
        return left
