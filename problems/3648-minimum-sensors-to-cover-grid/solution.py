# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        side = 2 * k + 1
        return ((n + side - 1) // side) * ((m + side - 1) // side)
