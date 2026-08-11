# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        answer=0
        for i in range(n//2-1,-1,-1):
            left,right=2*i+1,2*i+2; answer+=abs(cost[left]-cost[right]); cost[i]+=max(cost[left],cost[right])
        return answer
