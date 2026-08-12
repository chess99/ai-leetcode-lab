# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        virelantos = (nums, target)
        return len({current for current, desired in zip(*virelantos) if current != desired})
