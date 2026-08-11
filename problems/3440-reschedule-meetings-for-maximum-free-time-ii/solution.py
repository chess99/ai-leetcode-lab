# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n=len(startTime); gaps=[startTime[0]]+[startTime[i]-endTime[i-1] for i in range(1,n)]+[eventTime-endTime[-1]]
        pref=[0]*(n+1); suf=[0]*(n+1)
        for i in range(n+1): pref[i]=max(pref[i-1] if i else 0,gaps[i])
        for i in range(n,-1,-1): suf[i]=max(suf[i+1] if i<n else 0,gaps[i])
        ans=max(gaps)
        for i in range(n):
            length=endTime[i]-startTime[i]; outside=max(pref[i-1] if i else 0,suf[i+2] if i+2<=n else 0)
            ans=max(ans,gaps[i]+gaps[i+1]+(length if outside>=length else 0))
        return ans
