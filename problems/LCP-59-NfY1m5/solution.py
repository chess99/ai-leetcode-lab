# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
from typing import List
import heapq


class Solution:
    def buildBridge(self, num: int, wood: List[List[int]]) -> int:
        # Slope-trick representation of the convex cost for the current
        # log's left endpoint.  Heaps store breakpoints with lazy offsets.
        left, right = [], []
        left_add = right_add = answer = 0

        def add_absolute(a: int) -> None:
            nonlocal answer
            # Add max(0, a-x).
            if right and a > right[0] + right_add:
                x = heapq.heappop(right) + right_add
                answer += a - x
                heapq.heappush(right, a - right_add)
                heapq.heappush(left, -(x - left_add))
            else:
                heapq.heappush(left, -(a - left_add))

            # Add max(0, x-a).
            if left and a < -left[0] + left_add:
                x = -heapq.heappop(left) + left_add
                answer += x - a
                heapq.heappush(left, -(a - left_add))
                heapq.heappush(right, x - right_add)
            else:
                heapq.heappush(right, a - right_add)

        add_absolute(wood[0][0])
        previous_length = wood[0][1] - wood[0][0]
        for start, end in wood[1:]:
            length = end - start
            # Adjacent left endpoints may differ by any value in
            # [-length, previous_length]. This is an interval min-convolution.
            left_add -= length
            right_add += previous_length
            add_absolute(start)
            previous_length = length

        return answer
