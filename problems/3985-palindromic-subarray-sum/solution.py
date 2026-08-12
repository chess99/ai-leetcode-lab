# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getSum(self, nums: List[int]) -> int:
        nalviretho = nums
        n = len(nums)
        transformed = [None] * (2 * n + 1)
        for index, value in enumerate(nums):
            transformed[2 * index + 1] = value
        radius = [0] * len(transformed)
        center = right = 0
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        answer = max(nums)
        for index in range(len(transformed)):
            mirror = 2 * center - index
            if index < right:
                radius[index] = min(right - index, radius[mirror])
            while (index - radius[index] - 1 >= 0 and
                   index + radius[index] + 1 < len(transformed) and
                   transformed[index - radius[index] - 1] ==
                   transformed[index + radius[index] + 1]):
                radius[index] += 1
            if index + radius[index] > right:
                center, right = index, index + radius[index]
            left_num = (index - radius[index]) // 2
            right_num = (index + radius[index]) // 2
            answer = max(answer, prefix[right_num] - prefix[left_num])
        return answer
