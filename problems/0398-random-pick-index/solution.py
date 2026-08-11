# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:41Z
# Experiment: ai-leetcode-lab, round 1
import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        chosen = count = 0
        for index, value in enumerate(self.nums):
            if value == target:
                count += 1
                if random.randrange(count) == 0: chosen = index
        return chosen


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
