# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-15
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        size = len(nums)
        prefix_end = 0
        while (
            prefix_end + 1 < size
            and nums[prefix_end] < nums[prefix_end + 1]
        ):
            prefix_end += 1

        if prefix_end == size - 1:
            return size * (size + 1) // 2

        answer = prefix_end + 2
        compatible_prefix_end = prefix_end
        suffix_start = size - 1

        while (
            suffix_start == size - 1
            or nums[suffix_start] < nums[suffix_start + 1]
        ):
            while (
                compatible_prefix_end >= 0
                and nums[compatible_prefix_end] >= nums[suffix_start]
            ):
                compatible_prefix_end -= 1

            answer += compatible_prefix_end + 2
            suffix_start -= 1

        return answer
