# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:43Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        distance = [-1] * n
        distance[0] = 0
        queue = deque([0])
        left_boundary = 1
        while queue:
            node = queue.popleft()
            forward = node + jump[node]
            if forward >= n:
                return distance[node] + 1
            if distance[forward] == -1:
                distance[forward] = distance[node] + 1
                queue.append(forward)
            while left_boundary < node:
                if distance[left_boundary] == -1:
                    distance[left_boundary] = distance[node] + 1
                    queue.append(left_boundary)
                left_boundary += 1
