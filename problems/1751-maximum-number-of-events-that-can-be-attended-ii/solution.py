# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from bisect import bisect_right
        events.sort();starts=[x[0]for x in events];dp=[0]*(len(events)+1)
        for _ in range(k):
            nd=[0]*(len(events)+1)
            for i in range(len(events)-1,-1,-1):nd[i]=max(nd[i+1],events[i][2]+dp[bisect_right(starts,events[i][1])])
            dp=nd
        return dp[0]
