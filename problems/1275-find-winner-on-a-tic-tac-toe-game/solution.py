# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:45:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        for index, (row, column) in enumerate(moves):
            board[row][column] = 1 if index % 2 == 0 else -1
        lines = board + [[board[row][column] for row in range(3)] for column in range(3)]
        lines += [[board[0][0], board[1][1], board[2][2]],
                  [board[0][2], board[1][1], board[2][0]]]
        if any(sum(line) == 3 for line in lines):
            return "A"
        if any(sum(line) == -3 for line in lines):
            return "B"
        return "Draw" if len(moves) == 9 else "Pending"
