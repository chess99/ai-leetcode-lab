# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque(); answer = []
        for i, value in enumerate(nums):
            while queue and queue[0] <= i - k: queue.popleft()
            while queue and nums[queue[-1]] <= value: queue.pop()
            queue.append(i)
            if i >= k - 1: answer.append(nums[queue[0]])
        return answer
