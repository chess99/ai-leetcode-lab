# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:34Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        mod = 1_000_000_007
        if multiplier == 1:
            return [value % mod for value in nums]

        heap = [(value, index) for index, value in enumerate(nums)]
        heapify(heap)
        maximum = max(nums)

        while k and heap[0][0] * multiplier <= maximum:
            value, index = heap[0]
            heapreplace(heap, (value * multiplier, index))
            k -= 1

        ordered = sorted(heap)
        rounds, extra = divmod(k, len(nums))
        answer = [0] * len(nums)
        common_factor = pow(multiplier, rounds, mod)
        for rank, (value, index) in enumerate(ordered):
            result = value % mod * common_factor % mod
            if rank < extra:
                result = result * multiplier % mod
            answer[index] = result
        return answer
