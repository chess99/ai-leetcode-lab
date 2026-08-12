# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ferilonsar = nums
        latest = {}
        answer = len(nums) + 1
        for j, value in enumerate(ferilonsar):
            if value in latest:
                answer = min(answer, j - latest[value])
            reversed_value = int(str(value)[::-1])
            latest[reversed_value] = j
        return -1 if answer > len(nums) else answer
