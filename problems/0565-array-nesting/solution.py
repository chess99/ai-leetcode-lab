# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        longest = 0
        for start in range(len(nums)):
            if start in visited:
                continue
            length = 0
            current = start
            while current not in visited:
                visited.add(current)
                length += 1
                current = nums[current]
            longest = max(longest, length)
        return longest
