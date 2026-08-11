# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseByType(self, s: str) -> str:
        letters = iter(reversed([char for char in s if char.isalpha()]))
        specials = iter(reversed([char for char in s if not char.isalpha()]))
        return "".join(next(letters) if char.isalpha() else next(specials) for char in s)
