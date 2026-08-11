# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:57:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = best = 0
        for ch in s[:-1]:
            if ch == '0': zeros += 1
            else: ones -= 1
            best = max(best, zeros + ones)
        return best
