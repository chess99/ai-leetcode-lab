# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer=[]; cols=len(grid[0])
        for start in range(cols):
            col=start
            for row in grid:
                nxt=col+row[col]
                if nxt<0 or nxt==cols or row[nxt]!=row[col]:col=-1;break
                col=nxt
            answer.append(col)
        return answer
