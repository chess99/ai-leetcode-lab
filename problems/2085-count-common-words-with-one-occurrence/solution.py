# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a={word:words1.count(word) for word in words1};b={word:words2.count(word) for word in words2}
        return sum(a.get(word)==b.get(word)==1 for word in a)
