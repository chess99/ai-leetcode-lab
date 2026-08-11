# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort();end=farthest=count=i=0
        while end<time:
            while i<len(clips) and clips[i][0]<=end:farthest=max(farthest,clips[i][1]);i+=1
            if farthest==end:return -1
            end=farthest;count+=1
        return count
