# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, 1_000_000_007) - 2) % 1_000_000_007
