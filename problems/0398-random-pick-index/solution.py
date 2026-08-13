# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-13
# Experiment: ai-leetcode-lab, round 1
import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        positions = defaultdict(list)
        for index, value in enumerate(nums):
            positions[value].append(index)
        self.positions = positions

    def pick(self, target: int) -> int:
        return random.choice(self.positions[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
