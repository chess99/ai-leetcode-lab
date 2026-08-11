# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        best=current=0
        for value in arr*(2 if k>1 else 1):
            current=max(0,current+value); best=max(best,current)
        if k>2 and sum(arr)>0: best += (k-2)*sum(arr)
        return best % 1_000_000_007
