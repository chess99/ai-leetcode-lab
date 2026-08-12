# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:43Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = sorted(min(value, target) for value in flowers)
        size = len(flowers)
        incomplete = bisect_left(flowers, target)
        prefix = [0]
        for value in flowers:
            prefix.append(prefix[-1] + value)

        answer = 0
        completion_cost = 0
        for completed in range(size - incomplete, size + 1):
            remaining_count = size - completed
            if completion_cost > newFlowers:
                break
            remaining = newFlowers - completion_cost
            minimum = 0
            if remaining_count:
                low = flowers[0]
                high = target - 1
                while low < high:
                    middle = (low + high + 1) // 2
                    leveled = bisect_right(flowers, middle, 0, remaining_count)
                    cost = middle * leveled - prefix[leveled]
                    if cost <= remaining:
                        low = middle
                    else:
                        high = middle - 1
                minimum = low
            answer = max(answer, completed * full + minimum * partial)
            if remaining_count:
                completion_cost += target - flowers[remaining_count - 1]
        return answer
