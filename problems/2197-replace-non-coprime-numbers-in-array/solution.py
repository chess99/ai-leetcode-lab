# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:41Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for value in nums:
            stack.append(value)
            while len(stack) >= 2:
                common = gcd(stack[-2], stack[-1])
                if common == 1:
                    break
                right = stack.pop()
                left = stack.pop()
                stack.append(left // common * right)
        return stack
