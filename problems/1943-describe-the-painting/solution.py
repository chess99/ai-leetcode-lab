# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        changes=defaultdict(int)
        for start,end,color in segments:changes[start]+=color;changes[end]-=color
        answer=[];total=0;previous=None
        for point in sorted(changes):
            if previous is not None and total:answer.append([previous,point,total])
            total+=changes[point];previous=point
        return answer
