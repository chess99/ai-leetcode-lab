# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:25:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered=set()
        for left,right in nums:covered.update(range(left,right+1))
        return len(covered)
