# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts={}
        for char in s:counts[char]=counts.get(char,0)+1
        return len(set(counts.values()))==1
