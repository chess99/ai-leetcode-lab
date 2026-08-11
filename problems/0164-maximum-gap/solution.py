# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:27:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        lowest, highest = min(nums), max(nums)
        if lowest == highest:
            return 0
        width = max(1, (highest - lowest + len(nums) - 2) // (len(nums) - 1))
        count = (highest - lowest) // width + 1
        minimums = [float("inf")] * count
        maximums = [float("-inf")] * count
        for value in nums:
            index = (value - lowest) // width
            minimums[index] = min(minimums[index], value)
            maximums[index] = max(maximums[index], value)

        answer, previous = 0, maximums[0]
        for index in range(1, count):
            if minimums[index] != float("inf"):
                answer = max(answer, minimums[index] - previous)
                previous = maximums[index]
        return answer
