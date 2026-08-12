# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def count_less(limit):
            root = [None, None, 0]
            answer = 0
            for value in nums:
                node = root
                for bit in range(15, -1, -1):
                    value_bit = value >> bit & 1
                    limit_bit = limit >> bit & 1
                    if limit_bit:
                        same = node[value_bit]
                        if same:
                            answer += same[2]
                        node = node[value_bit ^ 1]
                    else:
                        node = node[value_bit]
                    if node is None:
                        break
                node = root
                node[2] += 1
                for bit in range(15, -1, -1):
                    value_bit = value >> bit & 1
                    if node[value_bit] is None:
                        node[value_bit] = [None, None, 0]
                    node = node[value_bit]
                    node[2] += 1
            return answer

        return count_less(high + 1) - count_less(low)
