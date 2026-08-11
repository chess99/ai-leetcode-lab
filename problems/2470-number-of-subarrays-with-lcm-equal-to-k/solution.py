# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:21Z
# Experiment: ai-leetcode-lab, round 1
from math import lcm
from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        answer = 0

        for start in range(len(nums)):
            current_lcm = 1

            for end in range(start, len(nums)):
                current_lcm = lcm(current_lcm, nums[end])

                if current_lcm == k:
                    answer += 1
                elif k % current_lcm != 0:
                    break

        return answer
