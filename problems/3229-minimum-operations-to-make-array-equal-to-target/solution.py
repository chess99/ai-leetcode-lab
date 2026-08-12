# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        differences = [wanted - current for current, wanted in zip(nums, target)]
        answer = abs(differences[0])
        for previous, current in zip(differences, differences[1:]):
            if previous * current > 0:
                answer += max(0, abs(current) - abs(previous))
            else:
                answer += abs(current)
        return answer
