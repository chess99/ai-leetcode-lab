# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        a=sorted(map(sorted,cuboids));dp=[]
        for i,x in enumerate(a):dp.append(x[2]+max([dp[j]for j,y in enumerate(a[:i])if all(y[t]<=x[t]for t in range(3))]+[0]))
        return max(dp)
