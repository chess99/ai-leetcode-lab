# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        coordinates = sorted({x for x, _, side in squares for x in (x, x + side)})
        index = {value: i for i, value in enumerate(coordinates)}
        events = []
        for x, y, side in squares:
            left, right = index[x], index[x + side]
            events.append((y, 1, left, right))
            events.append((y + side, -1, left, right))
        events.sort()

        segment_count = len(coordinates) - 1
        cover = [0] * (segment_count * 4 + 5)
        length = [0] * (segment_count * 4 + 5)

        def update(node: int, start: int, end: int, left: int, right: int, delta: int) -> None:
            if left <= start and end <= right:
                cover[node] += delta
            else:
                middle = (start + end) // 2
                if left < middle:
                    update(node * 2, start, middle, left, right, delta)
                if middle < right:
                    update(node * 2 + 1, middle, end, left, right, delta)
            if cover[node]:
                length[node] = coordinates[end] - coordinates[start]
            elif end - start == 1:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        slabs = []
        total_area = 0
        previous_y = events[0][0]
        event_index = 0
        while event_index < len(events):
            y = events[event_index][0]
            width = length[1]
            area = width * (y - previous_y)
            slabs.append((previous_y, y, width))
            total_area += area
            while event_index < len(events) and events[event_index][0] == y:
                _, delta, left, right = events[event_index]
                update(1, 0, segment_count, left, right, delta)
                event_index += 1
            previous_y = y

        half = total_area / 2
        below = 0
        for bottom, top, width in slabs:
            area = width * (top - bottom)
            if below + area >= half:
                if width == 0:
                    return float(bottom)
                return bottom + (half - below) / width
            below += area
        return float(previous_y)
