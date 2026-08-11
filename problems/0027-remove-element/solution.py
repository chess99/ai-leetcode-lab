# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:12:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for value in nums:
            if value != val:
                nums[write] = value
                write += 1
        return write
