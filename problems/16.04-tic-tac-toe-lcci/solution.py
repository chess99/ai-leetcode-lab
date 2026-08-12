# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        size = len(board)
        lines = list(board)
        lines.extend("".join(board[row][col] for row in range(size)) for col in range(size))
        lines.append("".join(board[i][i] for i in range(size)))
        lines.append("".join(board[i][size - 1 - i] for i in range(size)))
        for line in lines:
            if line[0] != " " and line == line[0] * size:
                return line[0]
        return "Pending" if any(" " in row for row in board) else "Draw"
