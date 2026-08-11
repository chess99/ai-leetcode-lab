# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:20:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + ord(char) - ord("A") + 1
        return result
