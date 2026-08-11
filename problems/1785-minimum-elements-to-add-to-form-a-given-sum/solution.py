# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(goal-sum(nums))+limit-1)//limit
