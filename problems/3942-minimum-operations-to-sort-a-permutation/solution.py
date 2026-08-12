# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dranofelik = nums
        n = len(nums)
        if n <= 2:
            return 0 if nums == list(range(n)) else 1

        if all(nums[i] == (nums[0] + i) % n for i in range(n)):
            start = nums[0]
        elif all(nums[i] == (nums[0] - i) % n for i in range(n)):
            start = n + nums[0]
        else:
            return -1

        distance = [-1] * (2 * n)
        distance[0] = 0
        queue = deque([0])
        while queue:
            state = queue.popleft()
            if state == start:
                return distance[state]
            orientation, shift = divmod(state, n)
            if orientation == 0:
                rotated = (shift - 1) % n
                reversed_state = n + (shift - 1) % n
            else:
                rotated = n + (shift + 1) % n
                reversed_state = (shift + 1) % n
            for next_state in (rotated, reversed_state):
                if distance[next_state] == -1:
                    distance[next_state] = distance[state] + 1
                    queue.append(next_state)
        return -1
