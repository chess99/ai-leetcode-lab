# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:37Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        sorelanuxi = nums
        answer = 0
        for bit in range(30):
            tails = []
            mask = 1 << bit
            for value in sorelanuxi:
                if value & mask:
                    index = bisect_left(tails, value)
                    if index == len(tails):
                        tails.append(value)
                    else:
                        tails[index] = value
            answer = max(answer, len(tails))
        return answer
