# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        positions=defaultdict(list); answer=0
        for i,x in enumerate(nums): positions[x].append(i)
        for arr in positions.values():
            left=0
            for right in range(len(arr)):
                while arr[right]-arr[left]-(right-left)>k: left+=1
                answer=max(answer,right-left+1)
        return answer
