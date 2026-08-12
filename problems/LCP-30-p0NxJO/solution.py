# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        health = 1
        delayed = []
        operations = 0
        for value in nums:
            health += value
            if value < 0:
                heapq.heappush(delayed, value)
            if health <= 0:
                worst = heapq.heappop(delayed)
                health -= worst
                operations += 1
        return operations
