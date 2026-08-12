# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        size = len(nums)
        prefix_end = 0
        while prefix_end + 1 < size and nums[prefix_end] < nums[prefix_end + 1]:
            prefix_end += 1
        if prefix_end == size - 1:
            return size * (size + 1) // 2
        answer = prefix_end + 2
        suffix_start = size - 1
        while suffix_start == size - 1 or nums[suffix_start] < nums[suffix_start + 1]:
            left = 0
            while left <= prefix_end and nums[left] < nums[suffix_start]:
                left += 1
            answer += left + 1
            if suffix_start == 0:
                break
            suffix_start -= 1
        return answer
