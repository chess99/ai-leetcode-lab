# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True);inventory.append(0);answer=0;mod=10**9+7
        for index in range(len(inventory)-1):
            count=index+1;levels=inventory[index]-inventory[index+1]
            if orders>=count*levels:
                answer+=count*(inventory[index]+inventory[index+1]+1)*levels//2;orders-=count*levels
            else:
                full,rest=divmod(orders,count);answer+=count*(inventory[index]+inventory[index]-full+1)*full//2+rest*(inventory[index]-full);break
        return answer%mod
