# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        return first.keys() == second.keys() and sorted(first.values()) == sorted(second.values())
