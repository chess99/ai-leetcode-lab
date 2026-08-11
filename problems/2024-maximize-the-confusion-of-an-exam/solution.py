# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest_after_changing(target: str) -> int:
            left = 0
            changes = 0
            best = 0
            for right, answer in enumerate(answerKey):
                changes += answer != target
                while changes > k:
                    changes -= answerKey[left] != target
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(longest_after_changing("T"),
                   longest_after_changing("F"))
