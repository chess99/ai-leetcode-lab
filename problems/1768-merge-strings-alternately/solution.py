# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:33:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for a, b in zip(word1, word2): result.extend((a, b))
        return ''.join(result) + word1[len(word2):] + word2[len(word1):]
