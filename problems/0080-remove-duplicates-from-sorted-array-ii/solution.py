# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:16:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for value in nums:
            if write < 2 or value != nums[write - 2]:
                nums[write] = value
                write += 1
        return write
