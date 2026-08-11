# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        ordered = sorted(nums)
        middle = (len(nums) + 1) // 2
        nums[::2] = ordered[:middle][::-1]
        nums[1::2] = ordered[middle:][::-1]
