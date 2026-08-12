# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:31Z
# Experiment: ai-leetcode-lab, round 1
from math import comb
from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        size = len(nums)
        left = [-1] * size
        right = [-1] * size
        for index in range(1, size):
            node = 0
            while True:
                if nums[index] < nums[node]:
                    if left[node] < 0:
                        left[node] = index
                        break
                    node = left[node]
                else:
                    if right[node] < 0:
                        right[node] = index
                        break
                    node = right[node]

        subtree_size = [0] * size
        ways = [1] * size
        traversal = [0]
        for node in traversal:
            if left[node] >= 0:
                traversal.append(left[node])
            if right[node] >= 0:
                traversal.append(right[node])
        for node in reversed(traversal):
            left_size = subtree_size[left[node]] if left[node] >= 0 else 0
            right_size = subtree_size[right[node]] if right[node] >= 0 else 0
            left_ways = ways[left[node]] if left[node] >= 0 else 1
            right_ways = ways[right[node]] if right[node] >= 0 else 1
            subtree_size[node] = left_size + right_size + 1
            ways[node] = (comb(left_size + right_size, left_size) *
                          left_ways * right_ways) % mod
        return (ways[0] - 1) % mod
