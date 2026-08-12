# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        dravonelik = grid

        def best_line(values, minimum_length=1):
            if minimum_length == 1:
                current = answer = values[0]
                for value in values[1:]:
                    current = max(value, current + value)
                    answer = max(answer, current)
                return answer
            current = answer = values[0] + values[1]
            for index in range(2, len(values)):
                current = max(values[index - 1] + values[index], current + values[index])
                answer = max(answer, current)
            return answer

        answer = max(best_line(row, 2) for row in grid)
        if len(grid) > 2 and len(grid[0]) > 2:
            answer = max(answer, max(max(row[1:-1]) for row in grid[1:-1]))
        for column in range(len(grid[0])):
            answer = max(answer, best_line([row[column] for row in grid], 2))
        return answer
