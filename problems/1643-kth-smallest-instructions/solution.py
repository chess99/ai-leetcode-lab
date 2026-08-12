# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:35Z
# Experiment: ai-leetcode-lab, round 1
from math import comb
from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        vertical,horizontal=destination;answer=[]
        while vertical or horizontal:
            if horizontal:
                starting_h=comb(vertical+horizontal-1,vertical)
                if k<=starting_h:answer.append('H');horizontal-=1;continue
                k-=starting_h
            answer.append('V');vertical-=1
        return ''.join(answer)
