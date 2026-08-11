# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(chr(ord("z") - sum(weights[ord(char) - ord("a")] for char in word) % 26) for word in words)
