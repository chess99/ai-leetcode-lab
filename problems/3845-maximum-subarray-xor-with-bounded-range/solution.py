# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:58Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        meloraxuni = (nums, k)
        maximum = deque()
        minimum = deque()
        counts = [[0, 0] for _ in range((1 << 16) - 1)]

        def add(value: int, delta: int) -> None:
            node = 0
            for bit in range(14, -1, -1):
                direction = value >> bit & 1
                counts[node][direction] += delta
                node = node * 2 + 1 + direction

        def best(value: int) -> int:
            node = result = 0
            for bit in range(14, -1, -1):
                direction = value >> bit & 1
                desired = direction ^ 1
                if counts[node][desired]:
                    result |= 1 << bit
                    direction = desired
                node = node * 2 + 1 + direction
            return result

        prefix = 0
        prefixes = [0]
        add(0, 1)
        left = 0
        answer = 0
        for right, value in enumerate(nums):
            while maximum and nums[maximum[-1]] <= value:
                maximum.pop()
            maximum.append(right)
            while minimum and nums[minimum[-1]] >= value:
                minimum.pop()
            minimum.append(right)
            while nums[maximum[0]] - nums[minimum[0]] > k:
                add(prefixes[left], -1)
                if maximum[0] == left:
                    maximum.popleft()
                if minimum[0] == left:
                    minimum.popleft()
                left += 1
            prefix ^= value
            prefixes.append(prefix)
            answer = max(answer, best(prefix))
            add(prefix, 1)
        return answer
