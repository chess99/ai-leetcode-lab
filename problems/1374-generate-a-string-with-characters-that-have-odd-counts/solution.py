# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:55:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n % 2 else 'a' * (n - 1) + 'b'
