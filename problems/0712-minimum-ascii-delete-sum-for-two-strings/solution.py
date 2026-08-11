# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:33:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        costs = [0]
        for char in s2:
            costs.append(costs[-1] + ord(char))

        for first_index, first_char in enumerate(s1, start=1):
            diagonal = costs[0]
            costs[0] += ord(first_char)
            for second_index, second_char in enumerate(s2, start=1):
                above = costs[second_index]
                if first_char == second_char:
                    costs[second_index] = diagonal
                else:
                    costs[second_index] = min(
                        costs[second_index] + ord(first_char),
                        costs[second_index - 1] + ord(second_char),
                    )
                diagonal = above
        return costs[-1]
