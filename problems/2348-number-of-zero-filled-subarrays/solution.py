# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:29Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        consecutive_zeros = 0

        for value in nums:
            if value == 0:
                consecutive_zeros += 1
                answer += consecutive_zeros
            else:
                consecutive_zeros = 0

        return answer
