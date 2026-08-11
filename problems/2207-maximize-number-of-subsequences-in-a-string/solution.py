# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first, second = pattern
        first_count = 0
        second_count = 0
        subsequences = 0

        for char in text:
            if char == second:
                subsequences += first_count
                second_count += 1
            if char == first:
                first_count += 1

        return subsequences + max(first_count, second_count)
