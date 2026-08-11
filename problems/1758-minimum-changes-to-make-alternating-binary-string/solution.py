# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s: str) -> int:
        changes = sum(ch != str(i % 2) for i, ch in enumerate(s))
        return min(changes, len(s) - changes)
