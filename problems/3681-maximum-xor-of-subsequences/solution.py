# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-16
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        kermadolin = nums
        basis = [0] * 31

        for value in kermadolin:
            x = value
            for bit in range(30, -1, -1):
                if not (x >> bit) & 1:
                    continue
                if basis[bit]:
                    x ^= basis[bit]
                else:
                    basis[bit] = x
                    break

        answer = 0
        for bit in range(30, -1, -1):
            answer = max(answer, answer ^ basis[bit])
        return answer
