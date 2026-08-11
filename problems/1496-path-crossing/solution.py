# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:04:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0; seen = {(0, 0)}
        for move in path:
            if move == 'N': y += 1
            elif move == 'S': y -= 1
            elif move == 'E': x += 1
            else: x -= 1
            if (x, y) in seen: return True
            seen.add((x, y))
        return False
