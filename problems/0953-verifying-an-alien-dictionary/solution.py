# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}
        return all([rank[ch] for ch in a] <= [rank[ch] for ch in b] for a, b in zip(words, words[1:]))
