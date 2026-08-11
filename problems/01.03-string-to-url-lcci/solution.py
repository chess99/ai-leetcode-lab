# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")
