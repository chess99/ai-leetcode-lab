# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = min(max(xCenter, x1), x2)
        y = min(max(yCenter, y1), y2)
        return (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2
