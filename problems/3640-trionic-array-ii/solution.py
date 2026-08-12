# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        neg=-10**30; up1=neg; down=neg; up2=neg; ans=neg
        for a,b in zip(nums,nums[1:]):
            nu1=max(a+b, up1+b) if a<b else neg
            nd=max(up1+b, down+b) if a>b else neg
            nu2=max(down+b, up2+b) if a<b else neg
            up1,down,up2=nu1,nd,nu2;ans=max(ans,up2)
        return ans
