# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-15
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        zero_run = 0
        one_run = 0

        for char in s:
            if char == "0":
                if one_run > 0:
                    zero_run = 0
                    one_run = 0
                zero_run += 1
            else:
                one_run += 1
                best = max(best, 2 * min(zero_run, one_run))

        return best
