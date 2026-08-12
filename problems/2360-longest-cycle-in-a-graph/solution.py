# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        seen={};ans=-1
        for s in range(len(edges)):
            if s in seen:continue
            cur={};u=s;step=0
            while u!=-1 and u not in seen:
                cur[u]=step;seen[u]=1;step+=1;u=edges[u]
            if u in cur:ans=max(ans,step-cur[u])
        return ans
