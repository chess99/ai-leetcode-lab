# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
