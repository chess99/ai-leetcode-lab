# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        bit_count = [0] * 31
        current = 0
        left = 0
        answer = len(nums) + 1

        def add(value: int) -> None:
            nonlocal current
            for bit in range(31):
                if value >> bit & 1:
                    bit_count[bit] += 1
                    current |= 1 << bit

        def remove(value: int) -> None:
            nonlocal current
            for bit in range(31):
                if value >> bit & 1:
                    bit_count[bit] -= 1
                    if bit_count[bit] == 0:
                        current &= ~(1 << bit)

        for right, value in enumerate(nums):
            add(value)
            while current >= k:
                answer = min(answer, right - left + 1)
                remove(nums[left])
                left += 1
        return answer if answer <= len(nums) else -1
