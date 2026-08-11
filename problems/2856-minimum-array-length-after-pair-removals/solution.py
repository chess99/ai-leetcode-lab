# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        most=max(Counter(nums).values()); n=len(nums)
        return 2*most-n if most*2>n else n%2
