# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # Sweep columns from left to right.  ``last[y]`` is the most recent
        # column containing a point at y.  When two consecutive points in the
        # current column have the same previous column, they close a rectangle.
        # A range maximum over the y-levels strictly between them tells whether
        # a point has appeared inside that rectangle after its left side.
        cols = defaultdict(list)
        for x, y in zip(xCoord, yCoord):
            cols[x].append(y)
        ys_all = sorted(set(yCoord))
        pos = {y: i for i, y in enumerate(ys_all)}
        size = 1
        while size < len(ys_all):
            size <<= 1
        tree = [-1] * (size * 2)

        def assign(index: int, value: int) -> None:
            index += size
            tree[index] = value
            index >>= 1
            while index:
                tree[index] = max(tree[index * 2], tree[index * 2 + 1])
                index >>= 1

        def range_max(left: int, right: int) -> int:
            """Maximum on the inclusive compressed interval, or -1 if empty."""
            if left > right:
                return -1
            left += size
            right += size
            result = -1
            while left <= right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if not (right & 1):
                    result = max(result, tree[right])
                    right -= 1
                left >>= 1
                right >>= 1
            return result

        last = [-1] * len(ys_all)
        answer = -1
        for x in sorted(cols):
            ys = cols[x]
            ys.sort()
            for low, high in zip(ys, ys[1:]):
                a, b = pos[low], pos[high]
                left_x = last[a]
                if left_x != -1 and left_x == last[b] and range_max(a + 1, b - 1) < left_x:
                    answer = max(answer, (x - left_x) * (high - low))
            # Apply this column only after all checks: points on its vertical
            # side must not be mistaken for points strictly inside a candidate.
            for y in ys:
                index = pos[y]
                last[index] = x
                assign(index, x)
        return answer
