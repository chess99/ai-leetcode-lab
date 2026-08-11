# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, s: str) -> int:
        return sum(min(index, len(s) - index) for index in range(1, len(s)) if s[index] != s[index - 1])
