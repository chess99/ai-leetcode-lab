# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        answer=0
        for mask in range(1<<len(requests)):
            if mask.bit_count()<=answer:continue
            balance=[0]*n
            for i,(source,target) in enumerate(requests):
                if mask>>i&1:balance[source]-=1;balance[target]+=1
            if not any(balance):answer=mask.bit_count()
        return answer
