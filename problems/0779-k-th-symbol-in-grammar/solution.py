# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() % 2
