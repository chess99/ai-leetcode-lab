# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:50Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def visit(index):
            best=1
            for direction in (-1,1):
                for following in range(index+direction,index+direction*(d+1),direction):
                    if not 0<=following<len(arr) or arr[following]>=arr[index]:break
                    best=max(best,1+visit(following))
            return best
        return max(map(visit,range(len(arr))))
