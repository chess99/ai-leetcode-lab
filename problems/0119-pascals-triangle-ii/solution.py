# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:16:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for current in range(2, rowIndex + 1):
            for index in range(current - 1, 0, -1):
                row[index] += row[index - 1]
        return row
