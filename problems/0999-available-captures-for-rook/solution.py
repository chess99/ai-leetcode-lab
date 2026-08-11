# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:22:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R': break
            else: continue
            break
        result = 0
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            x, y = r + dr, c + dc
            while 0 <= x < 8 and 0 <= y < 8 and board[x][y] == '.': x, y = x + dr, y + dc
            if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 'p': result += 1
        return result
