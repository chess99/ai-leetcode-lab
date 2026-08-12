# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:17Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        wexthorbin = nums
        n = len(wexthorbin)
        values = wexthorbin[:]
        previous = [i - 1 for i in range(n)]
        following = [i + 1 for i in range(n)]
        following[-1] = -1
        alive = [True] * n
        heap = [(values[i] + values[i + 1], i, i + 1)
                for i in range(n - 1)]
        heapq.heapify(heap)

        bad = sum(values[i] > values[i + 1] for i in range(n - 1))
        operations = 0
        while bad:
            while True:
                pair_sum, left, right = heapq.heappop(heap)
                if (alive[left] and alive[right] and following[left] == right
                        and values[left] + values[right] == pair_sum):
                    break

            before = previous[left]
            after = following[right]
            if before != -1:
                bad -= values[before] > values[left]
            bad -= values[left] > values[right]
            if after != -1:
                bad -= values[right] > values[after]

            values[left] += values[right]
            alive[right] = False
            following[left] = after
            if after != -1:
                previous[after] = left

            if before != -1:
                bad += values[before] > values[left]
                heapq.heappush(heap, (values[before] + values[left], before, left))
            if after != -1:
                bad += values[left] > values[after]
                heapq.heappush(heap, (values[left] + values[after], left, after))
            operations += 1

        return operations
