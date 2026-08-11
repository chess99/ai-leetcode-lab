# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        closing_needed = 0
        for char in s:
            if char == '(':
                if closing_needed % 2:
                    insertions += 1
                    closing_needed -= 1
                closing_needed += 2
            else:
                closing_needed -= 1
                if closing_needed < 0:
                    insertions += 1
                    closing_needed = 1
        return insertions + closing_needed
