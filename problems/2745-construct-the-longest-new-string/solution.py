# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 2 * (2 * min(x, y) + int(x != y) + z)
