# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:10Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        replacements = sorted(set(arr2))
        states = {-1: 0}
        for value in arr1:
            following = {}
            for previous, operations in states.items():
                if value > previous:
                    following[value] = min(following.get(value, operations), operations)
                index = bisect_right(replacements, previous)
                if index < len(replacements):
                    replacement = replacements[index]
                    following[replacement] = min(
                        following.get(replacement, operations + 1), operations + 1)
            states = following
            if not states:
                return -1
        return min(states.values())
