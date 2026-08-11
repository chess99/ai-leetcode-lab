# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        answer = 0
        for skip in range(-1, len(nums)):
            g, l = 0, 1
            for i, value in enumerate(nums):
                if i != skip:
                    g = gcd(g, value)
                    l = l * value // gcd(l, value)
            answer = max(answer, g * l)
        return answer
