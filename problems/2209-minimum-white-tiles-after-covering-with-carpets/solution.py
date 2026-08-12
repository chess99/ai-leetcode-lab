# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        size = len(floor)
        previous = [0] * (size + 1)
        for index, value in enumerate(floor, 1):
            previous[index] = previous[index - 1] + (value == "1")

        for _ in range(numCarpets):
            current = [0] * (size + 1)
            for index in range(1, size + 1):
                uncovered = current[index - 1] + (floor[index - 1] == "1")
                covered = previous[max(0, index - carpetLen)]
                current[index] = min(uncovered, covered)
            previous = current
        return previous[size]
