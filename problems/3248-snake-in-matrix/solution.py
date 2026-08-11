# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:48:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row = col = 0
        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            else:
                col += 1
        return row * n + col
