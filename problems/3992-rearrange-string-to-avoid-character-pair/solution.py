# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return y * s.count(y) + ''.join(char for char in s if char not in (x, y)) + x * s.count(x)
