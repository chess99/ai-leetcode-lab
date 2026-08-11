# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        answer = 0
        for start in range(len(nums) - len(pattern)):
            if all(
                (nums[start + i + 1] > nums[start + i]) - (nums[start + i + 1] < nums[start + i]) == expected
                for i, expected in enumerate(pattern)
            ):
                answer += 1
        return answer
