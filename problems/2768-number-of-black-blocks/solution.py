# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blocks=Counter()
        for x,y in coordinates:
            for a in (x-1,x):
                for b in (y-1,y):
                    if 0<=a<m-1 and 0<=b<n-1: blocks[a,b]+=1
        ans=[0]*5
        for count in blocks.values(): ans[count]+=1
        ans[0]=(m-1)*(n-1)-sum(ans[1:])
        return ans
