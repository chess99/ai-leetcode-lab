# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:23:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row = col = 0
        path = []
        for character in target:
            value = ord(character) - ord("a")
            target_row, target_col = divmod(value, 5)
            path.append("U" * max(0, row - target_row))
            path.append("L" * max(0, col - target_col))
            path.append("D" * max(0, target_row - row))
            path.append("R" * max(0, target_col - col))
            path.append("!")
            row, col = target_row, target_col
        return "".join(path)
