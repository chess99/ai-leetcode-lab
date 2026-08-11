# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter
        for i in range(len(word)):
            counts = Counter(word[:i] + word[i+1:])
            if len(set(counts.values())) == 1: return True
        return False
