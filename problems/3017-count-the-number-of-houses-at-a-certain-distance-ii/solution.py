# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        difference = [0] * (n + 2)

        def add(left, right):
            if left <= right:
                difference[left] += 1
                difference[right + 1] -= 1

        for first in range(1, n):
            shortcut_prefix = abs(first - x) + 1

            upper = min(y, n)
            if first + 1 <= upper:
                boundary = (shortcut_prefix + y + first) // 2
                direct_end = min(upper, boundary)
                if first + 1 <= direct_end:
                    add(1, direct_end - first)

                shortcut_start = max(first + 1, boundary + 1)
                if shortcut_start <= upper:
                    add(shortcut_prefix + y - upper,
                        shortcut_prefix + y - shortcut_start)

            right_start = max(first + 1, y + 1)
            if right_start <= n:
                if shortcut_prefix + first < y:
                    add(shortcut_prefix + right_start - y,
                        shortcut_prefix + n - y)
                else:
                    add(right_start - first, n - first)

        answer = []
        running = 0
        for distance in range(1, n + 1):
            running += difference[distance]
            answer.append(running * 2)
        return answer
