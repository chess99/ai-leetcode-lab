# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:10:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum=max(nums);return k*maximum+k*(k-1)//2
