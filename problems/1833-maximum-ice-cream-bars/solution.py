# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer=0
        for cost in sorted(costs):
            if cost>coins:break
            coins-=cost;answer+=1
        return answer
