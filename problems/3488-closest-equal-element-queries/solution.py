# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums); positions=defaultdict(list)
        for i,x in enumerate(nums):positions[x].append(i)
        ans=[-1]*n
        for indices in positions.values():
            if len(indices)==1:continue
            for j,index in enumerate(indices):
                prev=indices[j-1]; nxt=indices[(j+1)%len(indices)]
                ans[index]=min((index-prev)%n,(nxt-index)%n)
        return [ans[q] for q in queries]
