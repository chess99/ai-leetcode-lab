# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp={};ans=0
        for x in sorted(nums):
            a=dp.get(x,0)+1;b=dp.get(x-1,0)+1
            dp[x+1]=max(dp.get(x+1,0),a);dp[x]=max(dp.get(x,0),b);ans=max(ans,a,b)
        return ans
