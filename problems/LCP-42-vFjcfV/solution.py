# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
        buckets = defaultdict(list)
        for x, y in circles:
            buckets[(x // r, y // r)].append((x, y))

        answer = 0
        for x, y, toy_radius in toys:
            reach = r - toy_radius
            if reach < 0:
                continue
            cell_x, cell_y = x // r, y // r
            found = False
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for center_x, center_y in buckets.get((cell_x + dx, cell_y + dy), ()):
                        if (x - center_x) ** 2 + (y - center_y) ** 2 <= reach**2:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            answer += found
        return answer
