# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        deletions = list(range(len(word2) + 1))
        for first_index, first_char in enumerate(word1, start=1):
            previous_diagonal = deletions[0]
            deletions[0] = first_index
            for second_index, second_char in enumerate(word2, start=1):
                previous_row = deletions[second_index]
                if first_char == second_char:
                    deletions[second_index] = previous_diagonal
                else:
                    deletions[second_index] = 1 + min(
                        deletions[second_index], deletions[second_index - 1]
                    )
                previous_diagonal = previous_row
        return deletions[-1]
