# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        size=max(instructions)+1;tree=[0]*(size+1)
        def query(index):
            answer=0
            while index:answer+=tree[index];index-=index&-index
            return answer
        answer=0
        for i,value in enumerate(instructions):
            less=query(value);greater=i-query(value+1);answer+=min(less,greater)
            index=value+1
            while index<len(tree):tree[index]+=1;index+=index&-index
        return answer%1_000_000_007
