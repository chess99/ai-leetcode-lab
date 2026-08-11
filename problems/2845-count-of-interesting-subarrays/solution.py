# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counts=defaultdict(int,{0:1}); prefix=answer=0
        for x in nums:
            prefix=(prefix+(x%modulo==k))%modulo
            answer+=counts[(prefix-k)%modulo]; counts[prefix]+=1
        return answer
