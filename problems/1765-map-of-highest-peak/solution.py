# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        answer = [[-1] * cols for _ in range(rows)]
        queue = deque((r, c) for r in range(rows) for c in range(cols) if isWater[r][c])
        for r, c in queue: answer[r][c] = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and answer[nr][nc] < 0:
                    answer[nr][nc] = answer[r][c] + 1; queue.append((nr,nc))
        return answer
