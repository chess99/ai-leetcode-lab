# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for start in range(len(nums) - k + 1):
            frequency = {}
            for value in nums[start : start + k]:
                frequency[value] = frequency.get(value, 0) + 1
            top = sorted(frequency.items(), key=lambda item: (item[1], item[0]), reverse=True)[:x]
            answer.append(sum(value * count for value, count in top))
        return answer
