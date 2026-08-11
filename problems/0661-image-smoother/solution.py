# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:57:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, columns = len(img), len(img[0])
        result = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                total = count = 0
                for r in range(max(0, row - 1), min(rows, row + 2)):
                    for c in range(max(0, column - 1), min(columns, column + 2)):
                        total += img[r][c]
                        count += 1
                result[row][column] = total // count
        return result
