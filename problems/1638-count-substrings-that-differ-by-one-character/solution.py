# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        rows, columns = len(s), len(t)
        matching_prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        matching_suffix = [[0] * (columns + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                if s[row - 1] == t[column - 1]:
                    matching_prefix[row][column] = matching_prefix[row - 1][column - 1] + 1

        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                if s[row] == t[column]:
                    matching_suffix[row][column] = matching_suffix[row + 1][column + 1] + 1

        count = 0
        for row in range(rows):
            for column in range(columns):
                if s[row] != t[column]:
                    count += (matching_prefix[row][column] + 1) * (matching_suffix[row + 1][column + 1] + 1)

        return count
