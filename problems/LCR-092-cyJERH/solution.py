# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                flips = min(flips + 1, ones)
        return flips
