# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:10:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = zeros = ones = 0
        for char in s + '0':
            if char == '0':
                best = max(best, 2 * min(zeros, ones))
                zeros, ones = zeros + 1, 0
            else:
                ones += 1
        return best
