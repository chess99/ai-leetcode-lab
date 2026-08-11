# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        scores=nums[:]; queue=deque([0])
        for i in range(1,len(nums)):
            while queue[0]<i-k:queue.popleft()
            scores[i]+=scores[queue[0]]
            while queue and scores[queue[-1]]<=scores[i]:queue.pop()
            queue.append(i)
        return scores[-1]
