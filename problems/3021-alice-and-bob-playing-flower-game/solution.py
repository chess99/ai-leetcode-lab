# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2) * ((m + 1) // 2) + ((n + 1) // 2) * (m // 2)
