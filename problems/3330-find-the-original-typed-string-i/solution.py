# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(word[i] == word[i - 1] for i in range(1, len(word)))
