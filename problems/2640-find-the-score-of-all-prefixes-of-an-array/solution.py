# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        best = total = 0; ans = []
        for x in nums:
            best = max(best, x); total += x + best; ans.append(total)
        return ans
