# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:58Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side

        def coordinate(point: List[int]) -> int:
            x, y = point
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 3 * side - x
            return perimeter - y

        positions = sorted(map(coordinate, points))
        n = len(positions)
        doubled = positions + [value + perimeter for value in positions]

        def feasible(distance: int) -> bool:
            following = [0] * (2 * n + 1)
            next_index = 0
            for index, value in enumerate(doubled):
                next_index = max(next_index, index + 1)
                while next_index < 2 * n and doubled[next_index] < value + distance:
                    next_index += 1
                following[index] = next_index
            following[2 * n] = 2 * n

            jump_tables = [following]
            for _ in range((k - 1).bit_length() - 1):
                previous = jump_tables[-1]
                jump_tables.append([previous[previous[index]] for index in range(2 * n + 1)])

            for start in range(n):
                current = start
                steps = k - 1
                bit = 0
                while steps:
                    if steps & 1:
                        current = jump_tables[bit][current]
                    steps >>= 1
                    bit += 1
                if current < start + n and doubled[current] <= doubled[start] + perimeter - distance:
                    return True
            return False

        low, high = 0, side
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
