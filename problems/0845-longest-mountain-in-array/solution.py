# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:50:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        index = 1
        while index < len(arr) - 1:
            if arr[index - 1] < arr[index] > arr[index + 1]:
                left = right = index
                while left > 0 and arr[left - 1] < arr[left]: left -= 1
                while right + 1 < len(arr) and arr[right] > arr[right + 1]: right += 1
                longest = max(longest, right - left + 1)
                index = right
            index += 1
        return longest
