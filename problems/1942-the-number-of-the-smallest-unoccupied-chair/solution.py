# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:06Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events=sorted((start,end,i) for i,(start,end) in enumerate(times));free=[];used=[];next_chair=0
        for start,end,friend in events:
            while used and used[0][0]<=start:heapq.heappush(free,heapq.heappop(used)[1])
            chair=heapq.heappop(free) if free else next_chair
            if not free and chair==next_chair:next_chair+=1
            if friend==targetFriend:return chair
            heapq.heappush(used,(end,chair))
