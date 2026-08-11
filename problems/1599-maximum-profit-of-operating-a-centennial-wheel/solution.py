# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting=profit=best=turn=answer=0
        while turn<len(customers) or waiting:
            if turn<len(customers): waiting+=customers[turn]
            boarded=min(4,waiting);waiting-=boarded;turn+=1
            profit+=boarded*boardingCost-runningCost
            if profit>best:best=profit;answer=turn
        return answer if best else -1
