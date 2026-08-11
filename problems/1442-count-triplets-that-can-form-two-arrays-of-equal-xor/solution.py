# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count=defaultdict(int); total=defaultdict(int); prefix=answer=0
        count[0]=1; total[0]=0
        for index,value in enumerate(arr,1):
            prefix ^= value
            answer += count[prefix]*(index-1)-total[prefix]
            count[prefix]+=1; total[prefix]+=index
        return answer
