# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        upper = k
        answer = k * (k + 1) // 2

        for number in sorted(set(nums)):
            if number > upper:
                break

            answer -= number
            upper += 1
            answer += upper

        return answer
