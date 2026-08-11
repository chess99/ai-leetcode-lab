# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n=len(nums);dp=[float('inf')]*n
        for end in range(n):
            maximum=total=0
            for start in range(end,-1,-1):
                maximum=max(maximum,nums[start]);total+=nums[start]
                dp[end]=min(dp[end],maximum*(end-start+1)-total)
        for _ in range(k):
            next_dp=dp[:]
            for end in range(n):
                maximum=total=0
                for start in range(end,0,-1):
                    maximum=max(maximum,nums[start]);total+=nums[start]
                    next_dp[end]=min(next_dp[end],dp[start-1]+maximum*(end-start+1)-total)
            dp=next_dp
        return dp[-1]
