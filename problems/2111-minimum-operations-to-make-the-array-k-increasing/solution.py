# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:09Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        answer = 0
        for offset in range(k):
            tails = []
            sequence = arr[offset::k]
            for value in sequence:
                index = bisect_right(tails, value)
                if index == len(tails):
                    tails.append(value)
                else:
                    tails[index] = value
            answer += len(sequence) - len(tails)
        return answer
