# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:51Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target)==1:return target[0]==1
        heap=[-value for value in target];heapq.heapify(heap);total=sum(target)
        while True:
            largest=-heapq.heappop(heap);rest=total-largest
            if largest==1 or rest==1:return True
            if rest==0 or largest<=rest:return False
            previous=largest%rest
            if previous==0:return False
            heapq.heappush(heap,-previous);total=rest+previous
