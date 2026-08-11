# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord("a") + (k - 1).bit_count())
