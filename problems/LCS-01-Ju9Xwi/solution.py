# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def leastMinutes(self, n: int) -> int:
        bandwidth = 1
        minutes = 1
        while bandwidth < n:
            bandwidth *= 2
            minutes += 1
        return minutes
