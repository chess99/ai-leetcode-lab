# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        layer = min(xPos, yPos, num - 1 - xPos, num - 1 - yPos)
        side = num - 2 * layer
        before = num * num - side * side
        if xPos == layer:
            offset = yPos - layer
        elif yPos == num - 1 - layer:
            offset = side - 1 + xPos - layer
        elif xPos == num - 1 - layer:
            offset = 2 * (side - 1) + num - 1 - layer - yPos
        else:
            offset = 3 * (side - 1) + num - 1 - layer - xPos
        return (before + offset) % 9 + 1
