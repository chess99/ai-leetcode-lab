# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:11:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for value in nums[1:]:
            if value != nums[write - 1]:
                nums[write] = value
                write += 1
        return write
