# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counts=Counter();answer=0
        for value in nums:
            key=value-int(str(value)[::-1]);answer+=counts[key];counts[key]+=1
        return answer%(10**9+7)
