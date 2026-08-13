# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        sizes = []
        for r in range(len(land)):
            for c in range(len(land[0])):
                if land[r][c]:continue
                stack = [(r, c)]
                land[r][c] = 1
                size = 0
                while stack:
                    x, y = stack.pop()
                    size += 1
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            a,b=x+dx,y+dy
                            if 0 <= a < len(land) and 0 <= b < len(land[0]) and land[a][b] == 0:
                                land[a][b] = 1
                                stack.append((a, b))
                sizes.append(size)
        return sorted(sizes)
