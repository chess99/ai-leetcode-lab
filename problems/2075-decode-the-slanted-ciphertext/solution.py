# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        columns = len(encodedText) // rows
        decoded = []

        for start_column in range(columns):
            for row in range(min(rows, columns - start_column)):
                decoded.append(encodedText[row * columns + start_column + row])

        return ''.join(decoded).rstrip()
