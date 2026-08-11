# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (a + b + abs(a - b)) // 2
