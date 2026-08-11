# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        answer=0
        for peak in range(len(heights)):
            total=heights[peak]; current=heights[peak]
            for i in range(peak-1,-1,-1): current=min(current,heights[i]); total+=current
            current=heights[peak]
            for i in range(peak+1,len(heights)): current=min(current,heights[i]); total+=current
            answer=max(answer,total)
        return answer
