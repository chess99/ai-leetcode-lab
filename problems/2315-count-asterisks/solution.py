# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:20:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(part.count('*') for part in s.split('|')[::2])
