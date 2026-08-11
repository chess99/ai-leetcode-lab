# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:56:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)
