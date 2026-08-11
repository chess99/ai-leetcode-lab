# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else n // 2 if n % 2 == 0 else n
