# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue=deque();prefix=0;answer=len(nums)+1
        for index in range(len(nums)+1):
            if index:prefix+=nums[index-1]
            while queue and prefix-queue[0][1]>=k:
                old_index,_=queue.popleft();answer=min(answer,index-old_index)
            while queue and queue[-1][1]>=prefix:queue.pop()
            queue.append((index,prefix))
        return -1 if answer>len(nums) else answer
