# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def place(index: int) -> bool:
            while index < len(sequence) and sequence[index] != 0:
                index += 1
            if index == len(sequence):
                return True

            for value in range(n, 0, -1):
                if used[value]:
                    continue
                if value == 1:
                    sequence[index] = 1
                    used[value] = True
                    if place(index + 1):
                        return True
                    used[value] = False
                    sequence[index] = 0
                elif index + value < len(sequence) and sequence[index + value] == 0:
                    sequence[index] = sequence[index + value] = value
                    used[value] = True
                    if place(index + 1):
                        return True
                    used[value] = False
                    sequence[index] = sequence[index + value] = 0

            return False

        place(0)
        return sequence
