# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:50Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict,deque
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)==1:return 0
        positions=defaultdict(list)
        for i,value in enumerate(arr):positions[value].append(i)
        queue=deque([(0,0)]);seen={0}
        while queue:
            index,moves=queue.popleft()
            for following in positions.pop(arr[index],[])+[index-1,index+1]:
                if following==len(arr)-1:return moves+1
                if 0<=following<len(arr) and following not in seen:seen.add(following);queue.append((following,moves+1))
