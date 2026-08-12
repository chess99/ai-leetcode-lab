# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
        queue = deque()
        answer = []
        for index, height in enumerate(heights):
            while queue and heights[queue[-1]] <= height:
                queue.pop()
            queue.append(index)
            if queue[0] <= index - limit:
                queue.popleft()
            if index + 1 >= limit:
                answer.append(heights[queue[0]])
        return answer
