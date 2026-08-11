# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even,odd,parity,answer=1,0,0,0
        for value in arr:
            parity=(parity+value)%2
            if parity:answer+=even;odd+=1
            else:answer+=odd;even+=1
        return answer%(10**9+7)
