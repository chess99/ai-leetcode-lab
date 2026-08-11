# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for value in arr1:
            text = str(value)
            for end in range(1, len(text) + 1):
                prefixes.add(text[:end])
        answer = 0
        for value in arr2:
            text = str(value)
            for end in range(1, len(text) + 1):
                if text[:end] in prefixes:
                    answer = max(answer, end)
        return answer
