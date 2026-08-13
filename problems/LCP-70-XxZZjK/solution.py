# AI solution attribution
# Original creator: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Solver: Codex Desktop / gpt-5.6-sol / ultra / sol-ultra
# Experiment: ai-leetcode-lab, profile escalation
from typing import List


class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        answer: List[List[int]] = []

        for row in range(1, size):
            planted = list(range(2, 2 * row - 1, 4))
            remainder = row % 4
            if remainder == 1:
                planted.append(2 * row - 1)
            elif remainder == 2:
                planted[-1] = 2 * row - 1
            answer.extend([row, column] for column in planted)

        # Alternating planted cells make every gap on the bottom row turn
        # green immediately and start the upward sweep.
        answer.extend([size, column] for column in range(1, 2 * size, 2))
        return answer
